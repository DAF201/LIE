from error_and_exception import TIME_OUT_ERROR
from threading import Thread
from task import task
from gc import collect
from typing import Any
from task_queue import task_queue


class processor():

    def __init__(self, max_tasks: int = 5, max_pool_depth: int = 50) -> None:
        self.max_tasks = max_tasks
        self.max_pool_depth = max_pool_depth
        # task queue, hold all tasks and return task to run
        self.task_queue = task_queue(max_tasks, max_pool_depth)

    # start processing
    def run(self) -> None:
        pass

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
