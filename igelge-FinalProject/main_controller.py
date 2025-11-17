#I really enjoyed this project, as it was similar to the Products API I worked on during quarter
#while still having a few differences, the tokens while challenging were probably my favorite.
#Thank you for an amazing quarter!!
from fastapi import FastAPI, status, Security, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
from typing import List, Optional

from starlette.responses import HTMLResponse

from models.student_model import Student
import services.student_service as student_service
import services.token_service as token_service

app = FastAPI(
    title="* INFO 1511 - Final Project API *",
    version="1.0",
    description="API for managing students, classes, and authentication tokens!",
    contact={"name": "Isabella Elge", "email": "igelge@mail.mccneb.edu"},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#I had a few problems with it not sending the Token through (getting stuck at another header) because of that I added this,
#now the program captures the proper header with Authorization. I use it below in each individual method to ensure the program
# finds the right header.
api_key_header = APIKeyHeader(name="Authorization", auto_error=False)

def validate_token(token: Optional[str]) -> bool:
    if not token:
        return False
    #Had some issues with tokens on the Swagger API, I used this because online I read that bearer could be causing the issue.
    if token.lower().startswith("bearer "):
        #Assuming one space after "bearer "
        token = token[7:]
    return token_service.token_exists(token)

@app.get("/", summary="Root Endpoint")
def root():
    return {"message": "Welcome to the Products API! Go to /docs for Swagger UI."}

@app.get(
    "/students",
    response_model=List[Student],
    responses={
        200: {"description": "Successfully retrieved students"},
        400: {"description": "Bad Request - No students found"},
        401: {"description": "Unauthorized - Invalid token"},
        422: {"description": "Validation Error"},
    },
)
def get_students(authorization: Optional[str] = Security(api_key_header)):
    if not validate_token(authorization):
        raise HTTPException(status_code=401, detail="Unauthorized token")
    students = student_service.get_all_students()
    if not students:
        raise HTTPException(status_code=400, detail="No students found")
    return students


@app.get(
    "/student",
    response_model=Student,
    responses={
        200: {"description": "Successfully retrieved student"},
        400: {"description": "Bad Request - Student not found"},
        401: {"description": "Unauthorized - Invalid token"},
        422: {"description": "Validation Error"},
    },
)
def get_student(student_id: Optional[int] = None, authorization: Optional[str] = Security(api_key_header)):
    if not validate_token(authorization):
        raise HTTPException(status_code=401, detail="Unauthorized token")

    if student_id is None:
        students = student_service.get_all_students()
        if not students:
            raise HTTPException(status_code=400, detail="No students found")
        return students

    student = student_service.get_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=400, detail="Student not found")
    return student


@app.post(
    "/students/add",
    response_model=dict,
    responses={
        200: {"description": "Success - Student added successfully"},
        400: {"description": "Bad Request - Duplicate ID"},
        401: {"description": "Unauthorized - Invalid token"},
        422: {"description": "Validation Error"},
    },
)
def add_student(student: Student, authorization: Optional[str] = Security(api_key_header)):
    if not validate_token(authorization):
        raise HTTPException(status_code=401, detail="Unauthorized token")

    success = student_service.add_student(student)
    if not success:
        raise HTTPException(status_code=400, detail=f"Student with ID {student.id} already exists")

    return {"message": "Student added successfully"}


@app.post(
    "/students/update",
    response_model=dict,
    responses={
        200: {"description": "Success - Student updated successfully"},
        400: {"description": "Bad Request - Student not found"},
        401: {"description": "Unauthorized - Invalid token"},
        422: {"description": "Validation Error"},
    },
)
def update_student(student: Student, authorization: Optional[str] = Security(api_key_header)):
    if not validate_token(authorization):
        raise HTTPException(status_code=401, detail="Unauthorized token")

    success = student_service.update_student(student)
    if not success:
        raise HTTPException(status_code=400, detail=f"Student with ID {student.id} not found")

    return {"message": "Student updated successfully!"}