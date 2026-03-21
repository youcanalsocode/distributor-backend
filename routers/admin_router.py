from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta

from database import SessionLocal
from models.admin_model import Admin
from schemas.admin_schema import AdminLogin, Token
from utils.auth_utils import verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(
    prefix="/admin",
    tags=["Admin Authentication"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login", response_model=Token)
def login_admin(admin: AdminLogin):
    if admin.username != "vimekrestomart" or admin.password != "itisstillraining1012":
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Adding role "admin" to token
    access_token = create_access_token(
        data={"sub": admin.username, "role": "admin"}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
