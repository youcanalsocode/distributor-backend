from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal
import models.order_model as models
import schemas.order_schema as schemas
from utils.dependencies import get_current_admin, get_current_restaurant
from models.restaurant_model import Restaurant
from models.product_model import Product

router = APIRouter(prefix="/orders", tags=["Orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def _enrich_order(order, db: Session):
    """Populate computed fields from related models."""
    if order.restaurant:
        order.restaurant_name = order.restaurant.name
        order.restaurant_address = getattr(order.restaurant, 'address', None)
        order.restaurant_phone = getattr(order.restaurant, 'mobile', None)
        order.restaurant_email = getattr(order.restaurant, 'email', None)
    for item in order.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        item.product_name = product.name if product else None
    return order


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
    return _enrich_order(new_order, db)


@router.get("/my", response_model=List[schemas.OrderResponse])
def get_my_orders(
    db: Session = Depends(get_db),
    current_restaurant: Restaurant = Depends(get_current_restaurant)
):
    orders = (
        db.query(models.Order)
        .filter(models.Order.restaurant_id == current_restaurant.id)
        .order_by(models.Order.id.asc())
        .all()
    )
    return [_enrich_order(o, db) for o in orders]


@router.get("/", response_model=List[schemas.OrderResponse])
def get_all_orders(
    db: Session = Depends(get_db),
    admin: bool = Depends(get_current_admin)
):
    orders = db.query(models.Order).order_by(models.Order.id.asc()).all()
    return [_enrich_order(o, db) for o in orders]


@router.patch("/{order_id}/status", response_model=schemas.OrderResponse)
def update_order_status(
    order_id: int,
    payload: schemas.OrderStatusUpdate,
    db: Session = Depends(get_db),
    admin: bool = Depends(get_current_admin)
):
    allowed = {"pending", "confirmed", "dispatched", "delivered", "cancelled"}
    if payload.status.lower() not in allowed:
        raise HTTPException(status_code=400, detail=f"Invalid status. Allowed: {allowed}")

    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = payload.status.lower()
    db.commit()
    db.refresh(order)
    return _enrich_order(order, db)
