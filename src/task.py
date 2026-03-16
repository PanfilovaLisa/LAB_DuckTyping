class Task:
    id_count = 0
    def __init__(self, payload: any):
        Task.id_count+=1
        self.id = Task.id_count
        self.payload = payload