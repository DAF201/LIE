from error_and_exception import TIME_OUT_ERROR
from threading import Thread
from task import task
from gc import collect
from typing import Any
from task_queue import task_queue


class processor():

    def __init__(self, max_tasks: int = 5, max_pool_depth: int = 50) -> None:
        # max tasks running at same time
        self.max_tasks = max_tasks
        # max tasks hold
        self.max_pool_depth = max_pool_depth
        # task queue
        self.task_queue = task_queue()
        # total task count
        self.task_count = 0
        # running task count
        self.task_running = 0

    # start processing
    def run(self) -> None:
        self.task_processing_thread = Thread(target=self.execute)

    # add new task
    def new_task(self, task: task) -> None:
        pass

    # remove task
    def del_task(self, task: task) -> None:
        pass

    # execute task in pool
    def execute(self) -> Any:
        pass

    # destroy all task when exit
    def __del__(self) -> None:
        collect()
