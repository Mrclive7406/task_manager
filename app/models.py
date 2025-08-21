from sqlalchemy import Column, String, Text, Enum
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .enums import TaskStatus


Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(200), nullable=False)
    description = Column(Text, default="")
    status = Column(Enum(TaskStatus), default=TaskStatus.CREATED)
