# CRUD operations for OCR projects
from sqlalchemy.orm import Session

from app.schemas.ocr_project import ProjectCreate


def create_project(db: Session, project: ProjectCreate, owner_id: int):
    