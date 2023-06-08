# not being test yet
from task_tools import Thread, Event
from task_container import task_container
from task_timer import task_timer
from random import randint
from os import cpu_count

NUM_OF_CPU = cpu_count()


class task_handler:
    # ensure no extra created
    __num_of_handler__ = 0
    # list of task need to be done
    container = task_container()
    task_pool = []
    stop_flag = Event()

    def __init__(self) -> None:
        if self.__num_of_handler__ > 0:
            return
        self.main = Thread(target=self.run)

    def start(self):
        """start the handler"""
        # ensure handler run will end when need
        self.main.daemon = True
        self.run()
        # block handler for run to be execute in different thread
        self.stop_flag.wait()

    def run(self):
        """grab tasks from container and run with priority"""
        # check by priority
        while (True):
            if not self.container.is_empty(2):
                self.fill_task_pool(2)
            elif not self.container.is_empty(1):
                self.fill_task_pool(1)
            elif not self.container.is_empty(0):
                self.fill_task_pool(0)
            elif not self.container.is_empty(-1):
                self.fill_task_pool(-1)
            elif not self.container.is_empty(-2):
                self.fill_task_pool(-2)

    def fill_task_pool(self, target) -> None:
        # while has space
        while (len(self.task_pool) < NUM_OF_CPU):
            # get a random int from 0-2 to get from ring, stack, or queue, then pop a task out
            task = self.container.priority_container[target][randint(
                0, 127) % 3].pop()

            self.task_pool.append(task_timer(task))
        for task in self.task_pool:
            task.start()

    def terminate(self):
        """set flag to exit"""
        self.stop_flag.set()
