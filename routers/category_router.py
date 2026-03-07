from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import models.category_model as models
import schemas.category_schema as schemas
from database import SessionLocal

router = APIRouter(prefix="/categories", tags=["Categories"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE CATEGORY
@router.post("/")
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):

    new_category = models.Category(
        name=category.name,
        description=category.description
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category


# GET ALL CATEGORIES
@router.get("/", response_model=list[schemas.Category])
def get_categories(db: Session = Depends(get_db)):

    return db.query(models.Category).all()


# UPDATE CATEGORY
@router.put("/{category_id}")
def update_category(category_id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)):

    existing_category = db.query(models.Category).filter(models.Category.id == category_id).first()

    if not existing_category:
        raise HTTPException(status_code=404, detail="Category not found")

    existing_category.name = category.name
    existing_category.description = category.description

    db.commit()
    db.refresh(existing_category)

    return existing_category


# DELETE CATEGORY
@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):

    category = db.query(models.Category).filter(models.Category.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()

    return {"message": "Category deleted successfully"}