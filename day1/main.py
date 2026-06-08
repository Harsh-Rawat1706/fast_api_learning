from fastapi import FastAPI

app = FastAPI()

# student list

students = ["harsh", "satyarth", "satyam", "pratik", "sahil"]

# course list
courses = ["python", "java", "c++", "javascript", "ruby"]

@app.get("/")
def home():
    return {"message": "Welcome to the Student Course API!"}

@app.get("/students")
def get_students():
    return {"students": students}

@app.get("/courses")
def get_courses():
    return {"courses": courses}

@app.post("/students")
def add_student(student: str):
    students.append(student)
    return {"message": f"Student '{student}' added successfully!"}

@app.delete("/students")
def delete_student(student: str):
    if student in students:
        students.remove(student)
        return {"message": f"Student '{student}' removed successfully!"}
    else:
        return {"message": f"Student '{student}' not found!"}