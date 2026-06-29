from models.user_model import ChangePassword
from fastapi import APIRouter, HTTPException
from starlette import status
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
from models.user_model import UserRegister, UserLogin
#from API.database import users_collection
from .database import users_collection
import os
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

load_dotenv()

router=APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

secret_key=os.getenv("SECRET_KEY")
algorithm=os.getenv("JWT_ALGORITHM")
access_token_expire_minutes=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

def hash_password(password:str)-> str:
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str)->bool:
    return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data:dict)->str:
    to_encode= data.copy()
    expire = datetime.utcnow()+timedelta(minutes=int(access_token_expire_minutes))
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,secret_key,algorithm=algorithm)

@router.post("/register")
def register(user:UserRegister):
    existing_user= users_collection.find_one({"username":user.username})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exist"
        )
    hashed_pwd=hash_password(user.password)
    users_collection.insert_one({
    "username": user.username,
    "email": user.email,
    "password": hashed_pwd,        
    "created_at": datetime.utcnow()
})
    return {"message":"User registered successfully"}


@router.post("/login")
def login(user: UserLogin):
    # find user in database
    db_user = users_collection.find_one({"username": user.username})
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    if not verify_password(user.password,db_user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password",

        )
    token=create_access_token({"sub":user.username})
    return {
        "message": "User logged in successfully",
        "access_token":token,
        "token_type":"bearer",
        "user":user.username
        
    }
    

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.get("/profile")
def get_profile(current_user:str=Depends(get_current_user)):
    user=users_collection.find_one({"username":current_user})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return {
        "username": user["username"],
        "email": user["email"],
        "created_at": user["created_at"]
    }  

@router.post("/logout")
def logout(current_user:str=Depends(get_current_user)):
     return {"message": f"User {current_user} logged out successfully"}

@router.post("/change-password")
def change_password(request:ChangePassword,current_user:str=Depends(get_current_user)):
    user =users_collection.find_one({"username":current_user})
    if not verify_password(request.old_password,user["password"]):
        raise HTTPException(status_code=401, detail="Incorrect old password")
    new_hashed=hash_password(request.new_password)
    users_collection.update_one(
    {"username": current_user},
    {"$set": {"password": new_hashed}}  # ← make sure $set is there
)
    return {"message":"Password changed successfully"}

        
        






    
        

        
    


    
    
