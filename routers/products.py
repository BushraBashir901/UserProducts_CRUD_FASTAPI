from fastapi import APIRouter, Depends, HTTPException,Request
from sqlalchemy.orm import Session
from typing import List

from models import Products
from schemas import ProductsSchema 
from deps import get_db


routers=APIRouter(
    prefix='/products',
    tags=['Products']
)

@routers.post("/products", response_model=ProductsSchema)
def create_product(product: ProductsSchema, request: Request, db: Session = Depends(get_db)):

    new_product = Products(product_id=product.product_id, product_name=product.product_name)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


#show all product 
@routers.get("/products", response_model=List[ProductsSchema])
def show_products(db: Session = Depends(get_db)):
    return db.query(Products).all()


#updating exsiting products
@routers.put("/products/{product_id}", response_model=ProductsSchema)
def update_product(product_id: int, product: ProductsSchema, db: Session = Depends(get_db)):
    
    existing = db.query(Products).filter(Products.product_id == product_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Product not found")
    
    existing.product_name = product.product_name
    db.commit()
    db.refresh(existing)
    return existing


#Deleteing product 
@routers.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    
    existing = db.query(Products).filter(Products.product_id == product_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(existing)
    db.commit()
    return {"message": "Product deleted successfully"}

