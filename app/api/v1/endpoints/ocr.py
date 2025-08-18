# API routes for OCR functionalities

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/ocr", tags=["OCR"])

# pydantic model for product creation request body
class New_Project(BaseModel):
    project_name: str
    description: str | None = None

# to create a new ocr project
@router.post("/new")
async def create_new_project(new_project: New_Project):
    # print(f"{new_project.project_name} request recieved!!")
    return {"message": "Project successfully created!"}



# get a specific ocr project data by id
@router.get("/{project_id}/data")
async def get_ocr_project_data(project_id: int):
    # Ensure user has access to this ocr project data
    return {"project_id": project_id}

