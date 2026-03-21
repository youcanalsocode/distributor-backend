from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal
import models.order_model as models
import schemas.order_schema as schemas
from utils.dependencies import get_current_admin, get_current_restaurant
from models.restaurant_model import Restaurant

router = APIRouter(prefix="/orders", tags=["Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.OrderResponse)
def create_order(
    order: schemas.OrderCreate, 
    db: Session = Depends(get_db),
    current_restaurant: Restaurant = Depends(get_current_restaurant)
):
    new_order = models.Order(
        restaurant_id=current_restaurant.id,
        total_amount=order.total_amount
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for item in order.items:
        order_item = models.OrderItem(
            order_id=new_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price
        )
        db.add(order_item)
    
    db.commit()
    db.refresh(new_order)
    return new_order

@router.get("/", response_model=List[schemas.OrderResponse])
def get_all_orders(
    db: Session = Depends(get_db),
    admin: bool = Depends(get_current_admin)
):
    orders = db.query(models.Order).all()
    return orders
