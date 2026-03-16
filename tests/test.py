import pytest
from src import protocol, handler

def test_not_task_source():
    """Проверка, что объект не соотвутсвтует протоколу"""
    class Source:
        def __init__(self):
            ...
        

        def method(self):
            return 
    
    some_source = Source()
    
    print("----- Проверка соответствия протоколу -----")
    assert isinstance(some_source, protocol.TaskSource)==False

    print("----- Проверка, что из объекта не изымаются задачи -----")
    assert handler.TaskHandler(some_source) == False

