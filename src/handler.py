from src import protocol, log
import typing

def TaskHandler(source) -> None:
    if not isinstance(source, protocol.TaskSource):
        print("Ошибка. Объект не является источником.")
        log.log_in("ERROR: Объект не является источником задач.")
        return False
    
    tasks = source.get_tasks()
    for t in tasks:
        print(f"Задача № {t.id}. {t.payload}")
    log.log_in("SUCCESS")
    
    return True
