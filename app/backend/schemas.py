# backend/app/schemas.py

from pydantic import BaseModel, EmailStr
from typing import List, Optional
from uuid import UUID
from datetime import datetime

# Student Schemas
class StudentBase(BaseModel):
    name: str
    email: EmailStr

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: UUID
    created_at: datetime
    schedules: List["Schedule"] = []

    class Config:
        orm_mode = True

# Teacher Schemas
class TeacherBase(BaseModel):
    name: str
    email: EmailStr

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):
    id: UUID
    created_at: datetime
    schedules: List["Schedule"] = []

    class Config:
        orm_mode = True

# Schedule Schemas
class ScheduleBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime
    student_id: UUID
    teacher_id: UUID

class ScheduleCreate(ScheduleBase):
    pass

class Schedule(ScheduleBase):
    id: UUID
    created_at: datetime
    student: Student
    teacher: Teacher

    class Config:
        orm_mode = True

# Update for forward references
Student.update_forward_refs()
Teacher.update_forward_refs()
Schedule.update_forward_refs()
