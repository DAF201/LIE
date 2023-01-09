from task import task
from task_priority import priority


class task_queue:
    def __init__(self) -> None:
        self.queue = {0: [], 1: [], 2: [], 3: []}
        self.running = []

    def append(self, task: task, position: str = 'end'):
        pass

    def pop(self, task_id: str, priority: priority = 0):
        pass

    def insert(self):
        pass
