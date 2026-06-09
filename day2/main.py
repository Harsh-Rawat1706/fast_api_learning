from fastapi import FastAPI
from fastapi import Path , HTTPException

app = FastAPI()

students = dict({1: {"name": "Harsh", "age": 20, "course": "python"},
                 2: {"name": "Satyarth", "age": 21, "course": "java"},
                 3: {"name": "Satyam", "age": 22, "course": "c++"}})

@app.get("/")
def home():
    return {"message": "Welcome to the Student Course API!"}
@app.get("/get_students/{student_id}")
def get_students(student_id: int = Path(..., description="The ID of the student to retrieve", example=1)):
    if student_id in students:
        return students[student_id]
    raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found")

@app.post("/add_student/{name}/{age}/{course}")
def add_student(name: str, age: int, course: str):
    student = dict({"name": name, "age": age, "course": course})
    student_id = len(students) + 1
    students[student_id] = student
    return {"message": f"Student added successfully!", "student_id": student_id}

@app.delete("/delete_student/{student_id}")
def delete_student(student_id: int = Path(..., description="The ID of the student to delete", example=1)):
    if student_id in students:
        del students[student_id]
        return {"message": f"Student '{student_id}' removed successfully!"}
    raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found")