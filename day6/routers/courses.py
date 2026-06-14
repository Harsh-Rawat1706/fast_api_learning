from fastapi import APIRouter , Depends
from fastapi import Path , HTTPException ,Query
from schemas.courses import Course
from core.security import verify_token

cours = APIRouter()

courses = []

@cours.get("/get_courses")
def get_courses(username: str = Depends(verify_token)):
    return courses

@cours.post("/add_course")
def add_course(course: Course, username: str = Depends(verify_token)):

    courses.append(course.dict())
    return {"message": f"Course added successfully!", "course_id": len(courses)}