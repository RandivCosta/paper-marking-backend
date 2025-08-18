from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_new_project():
    response = client.post(
        "/ocr/new",
        json={"project_name": "invoice bill", "description": "convert sinhala invoice into english"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Project successfully created!"}

def test_get_ocr_project_data():
    response = client.get("/ocr/16/data")
    assert response.status_code == 200
    assert response.json() == {"project_id": 16}