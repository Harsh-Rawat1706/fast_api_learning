from fastapi import FastAPI
from fastapi import Path , HTTPException ,Query , Depends
from  fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm  # jwt authentication
from pydantic import BaseModel , Field , computed_field
from typing import Optional , Annotated , Literal
from routers.students import stud
from  routers.courses import cours
from routers.teachers import teach
from middleware.logger import log_request_time 
from  passlib.context import CryptContext  # password hashing

from jose import jwt, JWTError  # for JWT token generation
from datetime import datetime, timedelta, timezone  # for handling token expiration

app = FastAPI()

#jwt congifuration
SECRET_KEY = "mysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#password hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#OAuth2 configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

#fake user db
passu = pwd_context.hash("141706")
fake_users_db = {
    "harsh": {
        "username": "harsh",
        "password": passu,
    }
}

#hash password function
def hash_password(password: str):
    return pwd_context.hash(password)

#verify password function
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

#create token function
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

#login endpoint
@app.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm,Depends()]):
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_token({"sub": form_data.username})
    #generate JWT token here (omitted for brevity)
    return {"access_token": access_token, "token_type": "bearer"}

#token verification dependency
def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
#protected endpoint example
@app.get("/protected")
def protected_route(username: str = Depends(verify_token)):
    return {"message": f"Hello, {username}! This is a protected route."}

#middleware to log request time
app.middleware("http")(log_request_time)

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

app.include_router(stud)
app.include_router(cours)
app.include_router(teach)