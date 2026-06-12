from fastapi import APIRouter 
from fastapi import Path , HTTPException ,Query
from pydantic import BaseModel , Field , computed_field
from typing import Optional , Annotated , Literal


cours = APIRouter()

courses = []

class Course(BaseModel):
    name: Annotated[str, Field(...,description="The name of the course", example="Introduction to Python")]
    teacher: Annotated[str, Field(...,description="The teacher of the course", example="Jane Smith")]
    duration: Annotated[int, Field(...,gt=0,description="The duration of the course in weeks", example=12)]  # duration in weeks

@cours.get("/get_courses")
def get_courses():
    return courses

@cours.post("/add_course")
def add_course(course: Course):
    courses.append(course.dict())
    return {"message": f"Course added successfully!", "course_id": len(courses)}