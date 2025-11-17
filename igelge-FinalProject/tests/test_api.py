#I alternated between the @patch and non @patch tests just to play with it a bit
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main_controller import app, Student, student_service
from models.class_model import Class

client = TestClient(app)

sample_class = Class(
    id=1,
    code="INFO1511",
    title="Intro",
    description="Test class"
)

sample_student = Student(
    id=1,
    currentlyEnrolled=True,
    age=28,
    firstName="Test",
    lastName="Student",
    gender="female",
    email="test@student.com",
    phone="1234567890",
    address="123 Street",
    registered="2025-01-01",
    classes=[sample_class]
)

VALID_TOKEN = "abc123"


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]


@patch("main_controller.validate_token", return_value=True)
@patch("main_controller.student_service.get_all_students", return_value=[sample_student])
def test_get_students_mocked(mock_get_all_students, mock_validate):
    response = client.get("/students", headers={"Authorization": VALID_TOKEN})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["firstName"] == "Test"


def test_get_student_real_service():
    student_service.students = [] if hasattr(student_service, "students") else None
    student_service.add_student(sample_student)
    response = client.get(
        f"/student?student_id={sample_student.id}",
        headers={"Authorization": VALID_TOKEN}
    )
    assert response.status_code == 200
    assert response.json()["firstName"] == "Test"


@patch("main_controller.validate_token", return_value=True)
@patch("main_controller.student_service.add_student", return_value=True)
def test_add_student_mocked(mock_add_student, mock_validate):
    response = client.post(
        "/students/add",
        json=sample_student.dict(),
        headers={"Authorization": VALID_TOKEN},
    )
    assert response.status_code in [200, 201]
    assert "Student added successfully" in response.json()["message"]


def test_update_student_real_service():
    student_service.students = [] if hasattr(student_service, "students") else None
    student_service.add_student(sample_student)
    updated_student = sample_student.copy(update={"age": 22})
    response = client.post(
        "/students/update",
        json=updated_student.dict(),
        headers={"Authorization": VALID_TOKEN},
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Student updated successfully!"


@patch("main_controller.validate_token", return_value=False)
def test_unauthorized_access(mock_validate):
    response = client.get("/students", headers={"Authorization": "invalid"})
    assert response.status_code == 401
    assert "Unauthorized" in response.json()["detail"]
