from fastapi import FastAPI, HTTPException
from models import Student, UpdateStudent
from database import students

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI Student Management API 🚀"}

# GET all students
@app.get("/students")
def get_students():
    return students

# GET single student
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

# CREATE student
@app.post("/students")
def create_student(student: Student):
    students.append(student.dict())
    return {"message": "Student added successfully", "student": student}

# UPDATE student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_data: UpdateStudent):
    for student in students:
        if student["id"] == student_id:
            if updated_data.name is not None:
                student["name"] = updated_data.name
            if updated_data.age is not None:
                student["age"] = updated_data.age
            if updated_data.course is not None:
                student["course"] = updated_data.course
            return {"message": "Student updated", "student": student}
    raise HTTPException(status_code=404, detail="Student not found")

# DELETE student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {"message": "Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found")