from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Form
from sqlalchemy.orm import Session
from typing import Optional
import utils.file_utils as file_utils

import models.category_model as models
import schemas.category_schema as schemas
from database import SessionLocal
from utils.dependencies import get_current_admin

router = APIRouter(prefix="/categories", tags=["Categories"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE CATEGORY
@router.post("/", response_model=schemas.Category)
async def create_category(
    name: str = Form(...),
    description: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
    admin: bool = Depends(get_current_admin)
):
    image_url = None
    if image:
        image_url = file_utils.save_upload_file(image)

    new_category = models.Category(
        name=name,
        description=description,
        image_url=image_url
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category


# GET ALL CATEGORIES
@router.get("/", response_model=list[schemas.Category])
def get_categories(db: Session = Depends(get_db)):

    return db.query(models.Category).all()


# GET SINGLE CATEGORY
@router.get("/{category_id}", response_model=schemas.Category)
def get_category(category_id: int, db: Session = Depends(get_db)):

    category = db.query(models.Category).filter(models.Category.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


# UPDATE CATEGORY
@router.put("/{category_id}", response_model=schemas.Category)
async def update_category(
    category_id: int,
    name: str = Form(...),
    description: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
    admin: bool = Depends(get_current_admin)
):
    existing_category = db.query(models.Category).filter(models.Category.id == category_id).first()

    if not existing_category:
        raise HTTPException(status_code=404, detail="Category not found")

    existing_category.name = name
    existing_category.description = description

    if image:
        # Delete old image if it exists
        if existing_category.image_url:
            file_utils.delete_upload_file(existing_category.image_url)
        
        # Save new image
        existing_category.image_url = file_utils.save_upload_file(image)

    db.commit()
    db.refresh(existing_category)

    return existing_category


# DELETE CATEGORY
@router.delete("/{category_id}")
def delete_category(
    category_id: int, 
    db: Session = Depends(get_db),
    admin: bool = Depends(get_current_admin)
):

    category = db.query(models.Category).filter(models.Category.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    # Delete image file if it exists
    if category.image_url:
        file_utils.delete_upload_file(category.image_url)

    db.delete(category)
    db.commit()

    return {"message": "Category deleted successfully"}