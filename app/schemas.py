from pydantic import BaseModel, Field
from uuid import UUID
from .enums import TaskStatus


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200,
                       description="Короткое название задачи")
    description: str = Field("", max_length=200, description="Подробности")


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = Field(None, max_length=200)
    status: TaskStatus | None = None


class Task(TaskBase):
    id: UUID
    status: TaskStatus

    class Config:
        orm_mode = True
