from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name:str
    price:float

@app.get("/")
def home():
    return {"message": "Distributor Backend Running"}

@app.get("/products")
def get_products():
    return {"products": ["Frozen Chicken", "Frozen Fries", "Paneer Cubes"]}

@app.get("/restaurants")
def get_restaurants():
    return {"restaurants": ["Restaurant A", "Restaurant B"]}

@app.post("/products")
def create_product(product:Product):
    return {
        "message":"product created",
        "product":product
    }

@app.get("/products/{product_id}")
def get_productid(product_id:int):
    return {
        "productid":product_id,
        "message":"product created succesfully"
    }

@app.delete("/products/{delete_id}")
def delete_product_id(delete_id:int):
    return{
        "deleted id":delete_id,
        "message":"deleted succesful"
    }