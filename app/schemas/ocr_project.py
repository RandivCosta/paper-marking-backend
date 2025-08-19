# Contains Pydantic schemas for data validation and serialization
# These define the shape of request and response bodies

from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ProjectBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True # Pydantic can pull the attributes directly from the ORM object and return a proper response model
