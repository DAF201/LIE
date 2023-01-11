from task import task
from task_priority import priority


class task_queue:
    def __init__(self, max_tasks, max_pool_depth) -> None:
        self.queue = {0: [], 1: [], 2: [], 3: []}
        self.running = []
        self.waitlist = []
        self.current_pool_depth = 0

    def __iter__(self):

        return self

    def __next__(self) -> task:
        pass
