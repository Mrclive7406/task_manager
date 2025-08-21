from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID


from . import schemas, crud
from .database import SessionLocal, engine, Base


Base.metadata.create_all(bind=engine)


app = FastAPI(title="Task Manager", version="2.0.0")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/tasks", response_model=schemas.Task)
def create_task(task_in: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task_in)


@app.get("/tasks/{task_id}", response_model=schemas.Task)
def get_task(task_id: UUID, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.get("/tasks", response_model=list[schemas.Task])
def get_tasks(db: Session = Depends(get_db)):
    return crud.get_task_list(db)


@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: UUID, update_in: schemas.TaskUpdate,
                db: Session = Depends(get_db)):
    task = crud.update_task(db, task_id, update_in)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: UUID, db: Session = Depends(get_db)):
    if not crud.delete_task(db, task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"ok": True}
