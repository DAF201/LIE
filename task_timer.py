# unfinished
from task_body import task
from datetime import datetime, timedelta


class task_timer:
    def __init__(self, task: task) -> None:
        self.task = task
        self.start_time = datetime.now()
        self.expire_time = timedelta(self.task.time_out+self.start_time)

    def start(self):
        self.task.start()
