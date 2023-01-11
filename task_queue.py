from task import task
from task_priority import priority


class task_queue:
    def __init__(self) -> None:
        self.queue = {0: [], 1: [], 2: [], 3: []}
        self.running = []

    def append(self, task: task, position: str = 'end') -> None:
        pass

    def pop(self, task_id: str, priority: priority = 0) -> None:
        pass

    def get_task(self, task_id: str, priority: priority = 0) -> task:
        pass
