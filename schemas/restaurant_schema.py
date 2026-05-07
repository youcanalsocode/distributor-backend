from pydantic import BaseModel
from typing import Optional

class RestaurantCreate(BaseModel):
    mobile: str
    password: str
    name: str
    address: Optional[str] = None
    security_question: str
    security_answer: str

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

class SecurityQuestionResponse(BaseModel):
    security_question: str

class ResetPasswordRequest(BaseModel):
    mobile: str
    security_answer: str
    new_password: str
