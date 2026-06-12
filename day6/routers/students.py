from fastapi import APIRouter 
from fastapi import Path , HTTPException ,Query
from  schemas.students import Student

students = []

stud = APIRouter()

@stud.get("/get_students")
def get_students():
    return students

@stud.post("/add_student")
def add_student(student: Student):
    students.append(student.dict())
    return {"message": f"Student added successfully!", "student_id": len(students)}