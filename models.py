from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    course: Optional[str] = None