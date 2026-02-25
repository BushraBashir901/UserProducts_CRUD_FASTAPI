from sqlalchemy import Column, String, Integer, Boolean
from database import Base

# Create User model
class User(Base):
    __tablename__ = 'users'  # avoid reserved word
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    password=Column(String,nullable=False)
    
#Creatw Product model   
class Products(Base):
    __tablename__ = "products" 
    product_id=Column(Integer,primary_key=True)
    product_name=Column(String,nullable=False)