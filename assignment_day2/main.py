from fastapi import FastAPI , Path , HTTPException ,Query

app = FastAPI()

#student database
students = dict({1: {"name":"Harsh","age":20,"course":"B.Tech CSE"},
                 2: {"name":"Rahul","age":21,"course":"B.Tech IT"},
                 3: {"name":"Aman","age":22,"course":"B.Tech CSE"},
                 4: {"name":"Priya","age":20,"course":"BCA"},
                 5: {"name":"Anjali","age":21,"course":"MCA"}})
    
# teacher database 
teachers = dict({1: {"name": "Dr. Sharma", "subject": "DBMS"},
                 2: {"name": "Dr. Singh", "subject": "Operating Systems"},
                 3: {"name": "Dr. Gupta", "subject": "Computer Networks"}})

# course database
courses = dict({1: {"name": "DBMS", "semester": 4},
                 2: {"name": "Operating Systems", "semester": 5},
                 3: {"name": "Computer Networks", "semester": 5},
                 4: {"name": "Machine Learning", "semester": 7}})

@app.get("/")
def home():
    return {"message": "Welcome to the Student Course API!"}

#task1 -- create get api for teachers , course and students
@app.get("/get_data/dbname/{db_name}/id/{id}")
def get_data(db_name: str, id: int):
    if db_name == "students":
        if id in students:
            return students[id]
        raise HTTPException(status_code=404, detail=f"Student with ID {id} not found")
    elif db_name == "teachers":
        if id in teachers:
            return teachers[id]
        raise HTTPException(status_code=404, detail=f"Teacher with ID {id} not found")
    elif db_name == "courses":
        if id in courses:
            return courses[id]
        raise HTTPException(status_code=404, detail=f"Course with ID {id} not found")
    else:
        raise HTTPException(status_code=400, detail="Invalid database name. Must be 'students', 'teachers', or 'courses'.")

#task2 -- create get query api
@app.get("/get_dbname")
def get_dbname(db_name: str = Query(..., description="Name of the database to query"),sort_by: str = Query(default="name", description="The field to sort by (name, age, course, semester)"),order: str = Query(default="asc", description="The order to sort (asc or desc)")):
    if db_name == "students":
        data = list(students.values())
    elif db_name == "teachers":
        data = list(teachers.values())
    elif db_name == "courses":
        data = list(courses.values())
    else:
        raise HTTPException(status_code=400, detail="Invalid database name. Must be 'students', 'teachers', or 'courses'.")
    
    if sort_by not in ["name", "age", "course", "semester"]:
        raise HTTPException(status_code=400, detail="Invalid sort field. Must be one of 'name', 'age', 'course', or 'semester'.")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order. Must be 'asc' or 'desc'.")
    
    reverse_order = True if order == "desc" else False
    sorted_data = sorted(data, key=lambda x: x.get(sort_by, 0), reverse=reverse_order)
    return sorted_data