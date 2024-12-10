# backend/app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas

# Öğrenci CRUD İşlemleri
def get_student(db: Session, student_id: str):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Öğretmen CRUD İşlemleri
def get_teacher(db: Session, teacher_id: str):
    return db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()

def get_teachers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Teacher).offset(skip).limit(limit).all()

def create_teacher(db: Session, teacher: schemas.TeacherCreate):
    db_teacher = models.Teacher(name=teacher.name, email=teacher.email)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

# Ders Programı CRUD İşlemleri
def get_schedule(db: Session, schedule_id: str):
    return db.query(models.Schedule).filter(models.Schedule.id == schedule_id).first()

def get_schedules(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Schedule).offset(skip).limit(limit).all()

def create_schedule(db: Session, schedule: schemas.ScheduleCreate):
    db_schedule = models.Schedule(
        title=schedule.title,
        description=schedule.description,
        start_time=schedule.start_time,
        end_time=schedule.end_time,
        student_id=schedule.student_id,
        teacher_id=schedule.teacher_id
    )
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule
