from error_and_exception import TIME_OUT_ERROR
from threading import Thread
from task import task
from gc import collect


class processor():
    task_pool = {'0': [], '1': [], '2': [], '3': []}
    task_count = 0

    def __init__(self, max_task_running: int = 5, max_pool_depth: int = 50) -> None:
        pass

    # start processing
    def run(self):
        pass

    # add new task
    def new_task(self):
        pass

    # remove task
    def del_task(self):
        pass

    # destroy all task when exit
    def __del__(self):
        pass
