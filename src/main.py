import sys 
from .filesource import filesource
from .generator import generator
from .api import api
from src import handler, log
import os

def main():
    log.get_log()
    print("===== Приём задач из файла =====")
    log.log_in("Приём задач из файла")
    source_file = filesource.FileSource(os.path.join("src", "filesource", "tasks.txt"))
    handler.TaskHandler(source_file)

    print("\n===== Приём задач из генератора =====")
    log.log_in("Приём задач из генератора")
    source_generator = generator.TaskGenerator()
    handler.TaskHandler(source_generator)

    print("\n===== Приём задач из внешнего источника =====")
    log.log_in("Приём задач из внешнего источник")
    source_api = api.ApiSource()
    handler.TaskHandler(source_api)

    print("\n----- Обработка задач завершена -----")
    return
    


if __name__ == "__main__":
    main()