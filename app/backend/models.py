# backend/app/models.py
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from .database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(SQLUUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    schedules = relationship("Schedule", back_populates="student")


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(SQLUUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    schedules = relationship("Schedule", back_populates="teacher")


class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(SQLUUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    student_id = Column(SQLUUID(as_uuid=True), ForeignKey("students.id"))
    teacher_id = Column(SQLUUID(as_uuid=True), ForeignKey("teachers.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    student = relationship("Student", back_populates="schedules")
    teacher = relationship("Teacher", back_populates="schedules")
