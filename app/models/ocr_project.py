# contains ocr project database tables, inlcuding project details, resourses and user_id
import uuid
from app.db.database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func

class OCRProject(Base):
    __tablename__ = "ocr_project"

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer, nullable=False)
    title = Column(String, nullable= True)
    description = Column(Text, nullable= True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class OCRProjectFiles(Base):
    __tablename__ = "ocr_project_files"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("ocr_project.id"), nullable=False)
    file_uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4())) #unique id for each file to find the file in cloud
    file_name = Column(String(255), nullable=True)
    file_url = Column(String(1024), nullable=False)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())

