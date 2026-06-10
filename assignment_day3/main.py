from fastapi import FastAPI
from fastapi import Path , HTTPException ,Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

students = []
teachers = []
courses = []

class Student(BaseModel):
    name: str
    age: int
    course: str = "Data Science"  # default value for course is set to "Data Science"
    cgpa: float
    phone: Optional[str] = None  # Optional field for phone number
    
class Teacher(BaseModel):
    name: str
    age: int
    subject: str
    experience: int  # years of experience

class Course(BaseModel):
    name: str
    teacher: str
    duration: int  # duration in weeks
    
@app.get("/")
def home():
    return {"message": "Welcome to the Student Course API!"}

@app.get("/get_students")
def get_students():
    return students

@app.post("/add_student")
def add_student(student: Student):
    students.append(student.dict())
    return {"message": f"Student added successfully!", "student_id": len(students)}

@app.get("/get_teachers")
def get_teachers():
    return teachers

@app.post("/add_teacher")
def add_teacher(teacher: Teacher):
    teachers.append(teacher.dict())
    return {"message": f"Teacher added successfully!", "teacher_id": len(teachers)}

@app.get("/get_courses")
def get_courses():
    return courses

@app.post("/add_course")
def add_course(course: Course):
    courses.append(course.dict())
    return {"message": f"Course added successfully!", "course_id": len(courses)}