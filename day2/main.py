from fastapi import FastAPI
from fastapi import Path , HTTPException ,Query

app = FastAPI()

students = dict({1: {"name": "Harsh", "age": 20, "course": "python","cgpa": 9.5},
                 2: {"name": "Satyarth", "age": 21, "course": "java","cgpa": 8.5},
                 3: {"name": "Satyam", "age": 22, "course": "c++","cgpa": 9.0},
                 4: {"name": "yogesh", "age": 19, "course": "ML","cgpa": 7.5},
                 5: {"name": "Sahil", "age": 20, "course": "Data Science","cgpa": 8.7}})

@app.get("/")
def home():
    return {"message": "Welcome to the Student Course API!"}

@app.get("/get_students/{student_id}")
def get_students(student_id: int = Path(..., description="The ID of the student to retrieve", example=1)):
    if student_id in students:
        return students[student_id]
    raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found")

@app.get("/get_students")
def query_st(sort_by: str = Query(default="cgpa", description="The field to sort students by"),
              order: str = Query(default="desc", description="The order to sort students (asc or desc)")):
    
    if sort_by not in ["name", "age", "course", "cgpa"]:
        raise HTTPException(status_code=400, detail="Invalid sort field. Must be one of 'name', 'age', 'course', or 'cgpa'.")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order. Must be 'asc' or 'desc'.")
    tf = True if order == "desc" else False
    sorted_students = sorted(students.values(), key=lambda x: x.get(sort_by,0), reverse=tf)
    return  sorted_students

@app.post("/add_student/{name}/{age}/{course}/{cgpa}")
def add_student(name: str, age: int, course: str, cgpa: float):
    student = dict({"name": name, "age": age, "course": course, "cgpa": cgpa})
    student_id = len(students) + 1
    students[student_id] = student
    return {"message": f"Student added successfully!", "student_id": student_id}

@app.delete("/delete_student/{student_id}")
def delete_student(student_id: int = Path(..., description="The ID of the student to delete", example=1)):
    if student_id in students:
        del students[student_id]
        return {"message": f"Student '{student_id}' removed successfully!"}
    raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found")