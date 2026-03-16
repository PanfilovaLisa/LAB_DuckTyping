import typing
from src import task
import json
import os
import time

class ApiSource:
    def __init__(self):
        ...

    
    def get_tasks(self) -> typing.Iterable[task.Task]:
        print("Выполняется запрос...")

        with open(os.path.join("src", "api", "data.json")) as file:
            data = list(json.load(file))
            
        TaskList = [task.Task(tsk['payload']) for tsk in data]

        time.sleep(1)
        print(f"Ответ получен. Кол-во задач: {len(TaskList)}\n")

        return TaskList
