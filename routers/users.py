from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import User
from schemas import UserSchema, UserResponseSchema
from deps import get_db


routers=APIRouter(
    prefix="/users",
    tags=["User"]
)

        
#creating new user
@routers.post("/",response_model=UserResponseSchema)
def create_user(user:UserSchema,db:Session=Depends(get_db)):
    #add data into DB/table
    db_user = User(
        email=user.email, 
        is_active=user.is_active,
        password=str(user.password)
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Read all users
@routers.get("/", response_model=list[UserResponseSchema])
def read_users(db: Session = Depends(get_db)): #request:Request,
    #user_id = request.state.email
    return db.query(User).all()


#Accessing single user
@routers.get("/{user_id}", response_model=UserResponseSchema)
def single_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


#Update table    
@routers.put('/{user_id}',response_model=UserResponseSchema)
def update_user(user_id:int,updated_user:UserSchema, db:Session=Depends(get_db)):
    
    user=db.query(User).filter(User.id==user_id).first()
    
    if  not user:
       raise HTTPException(status_code=404)
    
    user.email = updated_user.email
    user.is_active = updated_user.is_active
    user.password=str(updated_user.password)
    
    db.commit()
    db.refresh(user)
    return user


#Delete table
@routers.delete('/{user_id}')
def delete_user(user_id:int,db:Session=Depends(get_db)):

    user=db.query(User).filter(User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404)
    
    db.delete(user)
    db.commit()
    return {'message':'User deleted Successfully '}
