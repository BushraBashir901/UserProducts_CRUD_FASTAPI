from typing import List,Optional
from pydantic import BaseModel,Field,EmailStr

#Schema for for entering data 
class UserSchema(BaseModel):
    id: Optional[int] = None
    email:EmailStr=Field(...,description='is Email of user?')
    password: str = Field(...,description="Password")
    is_active:bool=Field(...,description='is User account active?')
    
    model_config = {
    "from_attributes": True
}

#User Response schema 
class UserResponseSchema(BaseModel):
    id:int
    email:EmailStr
    is_active:bool
    
    model_config={
        "from_attributes":True
    }
    
#defining schema
class ProductsSchema(BaseModel):
    product_id:int
    product_name:str
    
    model_config={
        "from_attributes":True
    }       

#user login schema
class UserLoginSchema(BaseModel):
    email:EmailStr
    password:str 
    