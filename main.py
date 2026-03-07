from fastapi import FastAPI

from database import engine
from models import category_model, product_model

from routers import category_router, product_router

app = FastAPI()

category_model.Base.metadata.create_all(bind=engine)
product_model.Base.metadata.create_all(bind=engine)

app.include_router(category_router.router)
app.include_router(product_router.router)