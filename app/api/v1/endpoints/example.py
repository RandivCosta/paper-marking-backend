# app/api/v1/endpoints/projects.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.project import Project, ProjectCreate, ProjectUpdate
from app.crud import project as crud_project
from app.core.dependencies import get_db, get_current_user
from app.models.user import User

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model=Project, status_code=status.HTTP_201_CREATED)
def create_project(
    project: ProjectCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return crud_project.create_user_project(db=db, project=project, owner_id=current_user.id)

@router.get("/{project_id}", response_model=Project)
def read_project(
    project_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_project = crud_project.get_project(db, project_id=project_id)
    if db_project is None or db_project.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return db_project

@router.get("/", response_model=List[Project])
def read_user_projects(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    projects = crud_project.get_projects_by_owner(db, owner_id=current_user.id, skip=skip, limit=limit)
    return projects

@router.put("/{project_id}", response_model=Project)
def update_project(
    project_id: int,
    project_update: ProjectUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_project = crud_project.get_project(db, project_id=project_id)
    if db_project is None or db_project.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return crud_project.update_project(db=db, project_id=project_id, project_update=project_update)

@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(
    project_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_project = crud_project.get_project(db, project_id=project_id)
    if db_project is None or db_project.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    crud_project.delete_project(db=db, project_id=project_id)
    return {"message": "Project deleted successfully"}