from fastapi import FastAPI
from fastapi import Path , HTTPException ,Query , status , Depends
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

students = dict({1: {"name": "Harsh", "age": 20, "course": "python","cgpa": 9.5},
                 2: {"name": "Satyarth", "age": 21, "course": "java","cgpa": 8.5},
                 3: {"name": "Satyam", "age": 22, "course": "c++","cgpa": 9.0},
                 4: {"name": "yogesh", "age": 19, "course": "ML","cgpa": 7.5},
                 5: {"name": "Sahil", "age": 20, "course": "Data Science","cgpa": 8.7}})

# Custom Exception
def student_not_found(student_id: int):
    raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found")

def order_not_valid():
    raise HTTPException(status_code=400, detail=f"Invalid order. Must be 'asc' or 'desc'.")

# Dependency injection
def verify_token():
    print("token is verified")

# main page 
@app.get("/")
def home():
    return {"message": "Welcome to the Student Course API!"}

# response model 
class StudentResponse(BaseModel):
    name: str
    #age: int
    course: str
    #cgpa: float

@app.get("/get_students/{student_id}",summary = "Get a student by ID", description="Retrieve a student's details by their unique ID.")
def get_students(student_id: int = Path(..., description="The ID of the student to retrieve", example=1),auth: str = Depends(verify_token)):
    if student_id in students:
        return JSONResponse(status_code = status.HTTP_200_OK, content=StudentResponse(**students[student_id]).dict())
    student_not_found(student_id)

@app.get("/get_students",summary = "Get all students with sorting options", description="Retrieve a list of all students with optional sorting by name, age, course, or cgpa in ascending or descending order.")
def query_st(sort_by: str = Query(default="cgpa", description="The field to sort students by"),
              order: str = Query(default="desc", description="The order to sort students (asc or desc)")):
    
    if sort_by not in ["name", "age", "course", "cgpa"]:
        raise HTTPException(status_code=400, detail="Invalid sort field. Must be one of 'name', 'age', 'course', or 'cgpa'.")
    if order not in ["asc", "desc"]:
        order_not_valid()
    tf = True if order == "desc" else False
    sorted_students = sorted(students.values(), key=lambda x: x.get(sort_by,0), reverse=tf)
    return  sorted_students

# here we are creating a pydantic model to validate the input data for adding a student. 
# This ensures that the data is in the correct format and meets the required criteria before being added to the students dictionary.
class Student(BaseModel):
    name: str
    age: int
    course: str = "Data Science"  # default value for course is set to "Data Science"
    cgpa: float
    
@app.post("/add_student",summary = "Add a new student", description="Add a new student to the database with their name, age, course, and cgpa.")
def add_student(Student: Student):
    student = dict(Student)
    student_id = len(students) + 1
    students[student_id] = student
    return JSONResponse(status_code = status.HTTP_201_CREATED, content={"message": f"Student added successfully!", "student_id": student_id})

@app.delete("/delete_student/{student_id}",summary = "Delete a student", description="Delete a student from the database by their unique ID.")
def delete_student(student_id: int = Path(..., description="The ID of the student to delete", example=1)):
    if student_id in students:
        del students[student_id]
        return JSONResponse(status_code = status.HTTP_200_OK, content={"message": f"Student '{student_id}' removed successfully!"})
    student_not_found(student_id)