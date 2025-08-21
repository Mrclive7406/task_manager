from sqlalchemy.orm import Session
from . import models, schemas


def create_task(db: Session, task_in: schemas.TaskCreate):
    db_task = models.Task(title=task_in.title, description=task_in.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_task(db: Session, task_id):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_task_list(db: Session):
    return db.query(models.Task).all()


def update_task(db: Session, task_id, update_in: schemas.TaskUpdate):
    task = get_task(db, task_id)
    if not task:
        return None
    for field, value in update_in.dict(exclude_unset=True).items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id):
    task = get_task(db, task_id)
    if not task:
        return False
    db.delete(task)
    db.commit()
    return True
