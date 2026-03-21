from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta

from database import SessionLocal
from models.restaurant_model import Restaurant
from schemas.restaurant_schema import RestaurantCreate, RestaurantLogin, RestaurantResponse, Token
from utils.auth_utils import get_password_hash, verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(
    prefix="/restaurant",
    tags=["Restaurant Authentication"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=RestaurantResponse)
def register_restaurant(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    db_restaurant = db.query(Restaurant).filter(Restaurant.mobile == restaurant.mobile).first()
    if db_restaurant:
        raise HTTPException(status_code=400, detail="Mobile number already registered")
    
    hashed_password = get_password_hash(restaurant.password)
    new_restaurant = Restaurant(
        mobile=restaurant.mobile,
        name=restaurant.name,
        address=restaurant.address,
        password_hash=hashed_password
    )
    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)
    return new_restaurant

@router.post("/login", response_model=Token)
def login_restaurant(restaurant: RestaurantLogin, db: Session = Depends(get_db)):
    db_restaurant = db.query(Restaurant).filter(Restaurant.mobile == restaurant.mobile).first()
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="User not registered")
        
    if not verify_password(restaurant.password, db_restaurant.password_hash):
        raise HTTPException(status_code=401, detail="Incorrect password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": db_restaurant.mobile}, expires_delta=access_token_expires
    )
    return {
        "access_token": access_token, 
        "token_type": "bearer",
        "name": db_restaurant.name,
        "address": db_restaurant.address
    }
