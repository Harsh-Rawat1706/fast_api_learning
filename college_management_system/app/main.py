from fastapi import FastAPI

import app.models

from app.routers.department import router as department_router
from app.routers.user import router as user_router
from app.routers.student import router as student_router
from app.routers.teacher import router as teacher_router

app = FastAPI(
    title="College Management API",
    version="1.0.0",
)

app.include_router(department_router)
app.include_router(user_router)
app.include_router(student_router)
app.include_router(teacher_router)