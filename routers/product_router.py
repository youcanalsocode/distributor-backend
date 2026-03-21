from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Form
from sqlalchemy.orm import Session
from typing import Optional
import utils.file_utils as file_utils

import models.product_model as models
import schemas.product_schema as schemas
from database import SessionLocal
from utils.dependencies import get_current_admin

router = APIRouter(prefix="/products", tags=["Products"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Product)
async def create_product(
    name: str = Form(...),
    description: Optional[str] = Form(None),
    price: float = Form(...),
    stock: int = Form(...),
    category_id: int = Form(...),
    unit: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
    admin: bool = Depends(get_current_admin)
):
    image_url = None
    if image:
        image_url = file_utils.save_upload_file(image)

    new_product = models.Product(
        name=name,
        description=description,
        price=price,
        stock=stock,
        category_id=category_id,
        unit=unit,
        image_url=image_url
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


@router.get("/", response_model=list[schemas.Product])
def get_products(db: Session = Depends(get_db)):

    return db.query(models.Product).all()


@router.get("/{product_id}", response_model=schemas.Product)
def get_product(product_id: int, db: Session = Depends(get_db)):

    product = db.query(models.Product).filter(models.Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.put("/{product_id}")
async def update_product(
    product_id: int,
    name: str = Form(...),
    description: Optional[str] = Form(None),
    price: float = Form(...),
    stock: int = Form(...),
    category_id: int = Form(...),
    unit: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
    admin: bool = Depends(get_current_admin)
):
    existing_product = db.query(models.Product).filter(models.Product.id == product_id).first()

    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")

    existing_product.name = name
    existing_product.description = description
    existing_product.price = price
    existing_product.stock = stock
    existing_product.category_id = category_id
    existing_product.unit = unit

    if image:
        # Delete old image if it exists
        if existing_product.image_url:
            file_utils.delete_upload_file(existing_product.image_url)
        
        # Save new image
        existing_product.image_url = file_utils.save_upload_file(image)

    db.commit()
    db.refresh(existing_product)

    return existing_product


# DELETE PRODUCT
@router.delete("/{product_id}")
def delete_product(
    product_id: int, 
    db: Session = Depends(get_db),
    admin: bool = Depends(get_current_admin)
):

    product = db.query(models.Product).filter(models.Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Delete image file if it exists
    if product.image_url:
        file_utils.delete_upload_file(product.image_url)

    db.delete(product)
    db.commit()

    return {"message": "Product deleted"}