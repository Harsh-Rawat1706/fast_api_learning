from fastapi import APIRouter
from fastapi import Path , HTTPException ,Query
from schemas.teachers import Teacher

teach = APIRouter()

teachers = []

@teach.get("/get_teachers")
def get_teachers():
    return teachers

@teach.post("/add_teacher")
def add_teacher(teacher: Teacher):
    teachers.append(teacher.dict())
    return {"message": f"Teacher added successfully!", "teacher_id": len(teachers)}
