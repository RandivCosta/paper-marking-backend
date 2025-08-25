# CRUD operations for OCR projects
from sqlalchemy.orm import Session, joinedload

from app.models.ocr_project import OCRProject # db table classes
from app.schemas.ocr_project import ProjectCreate # validation data models

# get all ocr projects done by a user
# get a specific ocr project data

# to create a new ocr project
def create_new_project(db: Session, project: ProjectCreate, owner_id: int):
    db_project = OCRProject(**project.model_dump(), owner_id=owner_id)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

# to get ocr project data and project files data
def get_project_data(db:Session, projectId: int):
    project = db.query(OCRProject).options(joinedload(OCRProject.files)).filter(OCRProject.id == projectId).first()
    # print(project.__dict__)
    return project