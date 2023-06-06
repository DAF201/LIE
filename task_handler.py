from task_cycle_clock import clock
from task_container import *
from task_tools import *


class task_handler:
    num_of_task_handler = 0

    def __init__(self) -> None:
        if (self.num_of_task_handler != 0):
            del self
            return
        else:
            self.num_of_task_handler += 1
        self.ring = ring()
        