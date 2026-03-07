from pydantic import BaseModel

class ProductCreate(BaseModel):

    category_id: int

    name: str
    description: str

    price: float
    stock: int

    unit: str
    image_url: str