from fastapi import APIRouter 
from fastapi import Path , HTTPException ,Query
from pydantic import BaseModel , Field , computed_field
from typing import Optional , Annotated , Literal

students = []

stud = APIRouter()

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
        
@stud.get("/get_students")
def get_students():
    return students

@stud.post("/add_student")
def add_student(student: Student):
    students.append(student.dict())
    return {"message": f"Student added successfully!", "student_id": len(students)}