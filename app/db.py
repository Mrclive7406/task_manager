from uuid import uuid4
from typing import Dict
from .schemas import Task, TaskCreate
from .enums import TaskStatus

db: Dict[str, Task] = {}


def create_task(task_in: TaskCreate) -> Task:
    new_task = Task(
        id=uuid4(),
        title=task_in.title,
        description=task_in.description,
        status=TaskStatus.CREATED,
    )
    db[str(new_task.id)] = new_task
    return new_task


def get_task(task_id: str) -> Task | None:
    return db.get(task_id)


def get_task_list() -> list[Task]:
    return list(db.values())


def update_task(task_id: str, update_data) -> Task | None:
    task = db.get(task_id)
    if not task:
        return None
    updated = task.copy(update=update_data.dict(exclude_unset=True))
    db[task_id] = updated
    return updated


def delete_task(task_id: str) -> bool:
    return db.pop(task_id, None) is not None
