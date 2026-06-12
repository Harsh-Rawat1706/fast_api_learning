from fastapi import FastAPI
from fastapi import Path , HTTPException ,Query
from pydantic import BaseModel , Field , computed_field
from typing import Optional , Annotated , Literal
from routers.students import stud
from  routers.courses import cours
from routers.teachers import teach

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

app.include_router(stud)
app.include_router(cours)
app.include_router(teach)