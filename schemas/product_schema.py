from pydantic import BaseModel
from typing import Optional

# We need a basic Category schema to represent the category inside a product
class CategoryBase(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    unit: Optional[str] = None
    image_url: Optional[str] = None

class ProductCreate(ProductBase):
    category_id: int

class Product(ProductBase):
    id: int
    category_id: int
    category: CategoryBase

    class Config:
        from_attributes = True