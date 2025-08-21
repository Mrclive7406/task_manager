from enum import Enum


class TaskStatus(str, Enum):
    CREATED = "создано"
    IN_PROGRESS = "в работе"
    DONE = "завершено"
