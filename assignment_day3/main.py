from fastapi import FastAPI
from fastapi import Path , HTTPException ,Query
from pydantic import BaseModel , Field , computed_field
from typing import Optional , Annotated , Literal

app = FastAPI()

#Temporary Database 
students = []
teachers = []
courses = []

class Student(BaseModel):
    name: Annotated[str, Field(...,description="The name of the student", example="John Doe")]
    age: Annotated[int, Field(...,gt = 0,lt = 120,description="The age of the student", example=20)]
    course: Annotated[str, Field(..., description="The course the student is enrolled in", example="Data Science")]
    cgpa: Annotated[float, Field(...,ge=0.0,le=10.0, description="The CGPA of the student", example=8.5)]
    phone: Optional[str] = None  # Optional field for phone number
    @computed_field 
    @property
    def Grade(self) -> str:
        if self.cgpa >= 9.0:
            return "A"
        elif self.cgpa >= 8.0:
            return "B"
        elif self.cgpa >= 7.0:
            return "C"
        elif self.cgpa >= 6.0:
            return "D"
        else:
            return "F"
class Teacher(BaseModel):
    name: Annotated[str, Field(...,description="The name of the teacher", example="Jane Smith")]
    age: Annotated[int, Field(...,gt = 0,lt = 120,description="The age of the teacher", example=35)]
    subject: Annotated[str, Field(...,description="The subject the teacher teaches", example="Mathematics")]
    experience: Annotated[int, Field(...,ge=0,description="The years of experience the teacher has", example=10)]  # years of experience

class Course(BaseModel):
    name: Annotated[str, Field(...,description="The name of the course", example="Introduction to Python")]
    teacher: Annotated[str, Field(...,description="The teacher of the course", example="Jane Smith")]
    duration: Annotated[int, Field(...,gt=0,description="The duration of the course in weeks", example=12)]  # duration in weeks
    
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