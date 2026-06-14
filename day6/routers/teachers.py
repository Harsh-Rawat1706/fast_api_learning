from fastapi import APIRouter , Depends
from fastapi import Path , HTTPException ,Query
from schemas.teachers import Teacher
from core.security import verify_token

teach = APIRouter()

teachers = []

@teach.get("/get_teachers")
def get_teachers(username: str = Depends(verify_token)):
    return teachers

@teach.post("/add_teacher")
def add_teacher(teacher: Teacher, username: str = Depends(verify_token)):
    teachers.append(teacher.dict())
    return {"message": f"Teacher added successfully!", "teacher_id": len(teachers)}
