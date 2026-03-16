import typing
from src import task
import random 

class TaskGenerator:
    def __init__(self):
        self.tasks = {
            1: "Помыть посуду",
            2: "Пропылесосить комнаты",
            3: "Полить цветы",
            4: "Вынести мусор",
            5: "Сменить постельное бельё"
        }

    
    def get_tasks(self) -> typing.Iterable[task.Task]:
        TaskList = []
        while self.tasks:
            num = random.randint(1, 5)
            try:
                tsk = task.Task(self.tasks[num])
                TaskList+=[tsk]
                del self.tasks[num]
            except:
                ...
        return TaskList
