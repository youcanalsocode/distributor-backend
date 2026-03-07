from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/products")
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):

    new_product = models.Product(
        name=product.name,
        price=product.price
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return {
        "message": "Product created",
        "product_id": new_product.id
    }

@app.get("/products")
def get_products(db:Session=Depends(get_db)):
    products=db.query(models.Product).all()
    return products

@app.get("/products/{product_id}")
def get_product_byId(product_id:int ,db:Session=Depends(get_db)):
    product=db.query(models.Product).filter(models.Product.id ==product_id).first()
    if not product:
        return {"error": "Product not found"}

    return product

@app.delete("/products/{product_id}")
def delete_product_byId(product_id:int ,db:Session=Depends(get_db)):
    product=db.query(models.Product).filter(models.Product.id ==product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {
        "message": "Product deleted",
        
    }

@app.put("/products/{product_id}")
def updateby_id(product_id:int,product: schemas.ProductCreate,db:Session=Depends(get_db)):
    existing_product=db.query(models.Product).filter(models.Product.id==product_id).first()
    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    existing_product.name=product.name
    existing_product.price=product.price
    db.commit()
    db.refresh(existing_product)
    return {
        "message": "Product updated successfully",
        "product": existing_product
    }
    
    
