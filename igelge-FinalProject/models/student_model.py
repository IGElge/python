from pydantic import BaseModel
from typing import List
from models.class_model import Class

class Student(BaseModel):
    id: int
    currentlyEnrolled: bool
    age: int
    firstName: str
    lastName: str
    gender: str
    email: str
    phone: str
    address: str
    registered: str
    classes: List[Class]
