import typing
from src import task

@typing.runtime_checkable
class TaskSource(typing.Protocol):
    """Источник задач должен уметь возвращать задачи"""
    def __init__(self):
        ...

    
    def get_tasks(self) -> typing.Iterable[task.Task]:
        """Возращает задачи"""
        ...
