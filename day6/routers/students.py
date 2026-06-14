from fastapi import APIRouter , Depends
from fastapi import Path , HTTPException ,Query
from  schemas.students import Student
from core.security import verify_token

students = []

stud = APIRouter()

@stud.get("/get_students")
def get_students(username: str = Depends(verify_token)):
    return students

@stud.post("/add_student")
def add_student(student: Student, username: str = Depends(verify_token)):
    students.append(student.dict())
    return {"message": f"Student added successfully!", "student_id": len(students)}