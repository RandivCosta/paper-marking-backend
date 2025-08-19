# API routes for OCR functionalities

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.schemas.ocr_project import Project, ProjectCreate
from app.crud import ocr_project as crud_ocr_project

router = APIRouter(prefix="/ocr", tags=["OCR"])

# to create a new ocr project
@router.post("/new", response_model=Project, tatus_code=status.HTTP_201_CREATED)
async def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return crud_ocr_project.create_project(db=db, project=project, owner_id=5) # pass a integer for id for now.later change it to current user id.

# get a specific ocr project data by id
@router.get("/{project_id}/data")
async def get_ocr_project_data(project_id: int):
    # Ensure user has access to this ocr project data
    return {"project_id": project_id}

