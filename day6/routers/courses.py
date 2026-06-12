from fastapi import APIRouter 
from fastapi import Path , HTTPException ,Query
from schemas.courses import Course


cours = APIRouter()

courses = []

@cours.get("/get_courses")
def get_courses():
    return courses

@cours.post("/add_course")
def add_course(course: Course):
    courses.append(course.dict())
    return {"message": f"Course added successfully!", "course_id": len(courses)}