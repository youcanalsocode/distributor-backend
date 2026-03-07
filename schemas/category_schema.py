from pydantic import BaseModel
from typing import List, Optional

# We need a basic Product schema to represent products inside a category
class ProductBase(BaseModel):
    id: int
    name: str
    price: float
    stock: int

    class Config:
        from_attributes = True

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    products: List[ProductBase] = []

    class Config:
        from_attributes = True