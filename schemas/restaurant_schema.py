from pydantic import BaseModel
from typing import Optional

class RestaurantCreate(BaseModel):
    mobile: str
    password: str
    name: str
    address: Optional[str] = None

class RestaurantLogin(BaseModel):
    mobile: str
    password: str

class RestaurantResponse(BaseModel):
    id: int
    mobile: str
    name: str
    address: Optional[str] = None

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
    name: str
    address: Optional[str] = None
