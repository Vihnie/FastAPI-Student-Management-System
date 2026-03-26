

&#x20;Prompt-Powered Kickstart: Building a Beginner’s Toolkit for FastAPI

1\. Title \& Objective



&#x20;Title:



Getting Started with FastAPI – A Beginner’s Guide to Building a Student Management API



Objective:



The goal of this project was to learn FastAPI using Generative AI prompts and build a simple but functional Student Management REST API.



The final outcome is a working CRUD API with:



\* Input validation

\* Error handling

\* Auto-generated API documentation

\* Clear setup instructions for beginners





&#x20;2. Quick Summary of FastAPI



FastAPI is a modern, high-performance Python web framework used for building APIs quickly and efficiently.



&#x20;What is it?



FastAPI is a backend framework built on top of:



\* Starlette (for web handling)

\* Pydantic (for data validation)



&#x20;Where is it used?



\* AI startups

\* Microservices

\* Backend systems

\* High-performance APIs



Real-world Example:



Companies building AI-based systems use FastAPI to expose machine learning models as APIs.







3\. System Requirements



\* OS: Windows

\* Python 3.9+

\* Command Prompt

\* Internet connection

\* VS Code or Notepad

\* pip (Python package manager)





4\. Installation \& Setup Instructions



Step 1: Check Python Installation



```bash

python --version

```



Step 2: Create Project Folder



```bash

mkdir fastapi-toolkit

cd fastapi-toolkit

```



&#x20;Step 3: Create Virtual Environment



```bash

python -m venv venv

venv\\Scripts\\activate

```



&#x20;Step 4: Install Dependencies



```bash

pip install fastapi uvicorn

```



&#x20;Step 5: Run the Server



```bash

uvicorn main:app --reload

```



Open in browser:





http://127.0.0.1:8000/docs





5\. Minimal Working Example

&#x20;What the Example Does



The Student Management API allows users to:



\* Add a student

\* View all students

\* Get a student by ID

\* Update student information

\* Delete a student



\### Sample Code (main.py)



```python

from fastapi import FastAPI, HTTPException

from models import Student, UpdateStudent

from database import students



app = FastAPI()



@app.get("/")

def home():

&#x20;   return {"message": "Welcome to the FastAPI Student Management API"}



@app.get("/students")

def get\_students():

&#x20;   return students



@app.post("/students")

def create\_student(student: Student):

&#x20;   students.append(student.dict())

&#x20;   return {"message": "Student added", "student": student}

```



Expected Output



\* JSON responses in browser

\* Swagger UI documentation

\* Proper validation errors if wrong input is given







6\. AI Prompt Journal



Prompt 1:



“Give me a step-by-step guide to set up FastAPI on Windows.”



AI Help Summary:

The AI provided environment setup instructions including virtual environments and installing dependencies.



Helpfulness:

Very helpful in quickly scaffolding the project environment.



Prompt 2:



“Create a minimal FastAPI CRUD API for managing students.”



AI Help Summary:

Generated a structured CRUD API with GET, POST, PUT, DELETE endpoints.



Helpfulness:

Helped accelerate backend structure creation.





Prompt 3:



“Why is uvicorn saying ‘Attribute app not found’?”



AI Help Summary:

Identified that the main.py file was empty and not saved properly.



Helpfulness:

Critical debugging support. Prevented wasted time.







Reflection on AI Usage



Using AI significantly improved:



\* Setup speed

\* Debugging efficiency

\* Understanding FastAPI structure



However, manual verification (checking files, confirming saves, restarting server) was still necessary. AI speeds up learning but does not replace debugging discipline.





7\. Common Issues \& Fixes



Issue 1: “Attribute app not found in module main”



Cause:



\* main.py was empty or not saved correctly.



Fix:



\* Save file properly.

\* Confirm with `type main.py`.



Issue 2: Old API Still Showing



Cause:



\* Server not restarted.



Fix:



\* Stop server using CTRL+C.

\* Restart uvicorn.



Issue 3: Windows Saving as main.py.txt



Cause:



\* Notepad default save type.



Fix:



\* Choose “All Files” when saving.



&#x20;8. References



\* FastAPI Official Docs: \[https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)

\* Uvicorn Docs: \[https://www.uvicorn.org](https://www.uvicorn.org)

\* Pydantic Docs: \[https://docs.pydantic.dev](https://docs.pydantic.dev)







