import typing
from src import task, log

class FileSource:
    """Задачи, загружаемые из файла"""
    def __init__(self, path):
        self.path = path 

    
    def get_tasks(self) -> typing.Iterable[task.Task]:
        TaskList=[]
        try:
            with open(self.path) as file:
                for line in file.readlines():
                    tsk = task.Task(line.strip())
                    TaskList += [tsk]
            return TaskList
        except:
            print("Данного файла не существует.")
            log.log_in("ERROR: Данного файла не существует.")
