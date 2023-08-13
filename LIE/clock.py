from LIE.task import task
from LIE.priority import priority
from time import time, sleep
from gc import collect


class clock(priority):
    def __init__(self, task: task, priority=1, timeout=None, interval=1) -> None:
        super().__init__()
        self.__task = task
        self.__timeout = timeout
        self.__interval = interval
        self.__paused = True
        self.__terminated = False
        self.__priority = priority

    def __clock(self):
        while (not self.__terminated and time() < self.end):
            sleep(self.__interval)
        if not self.__paused:
            self.terminate()
        collect()

    def start(self):
        if not self.__paused:
            return
        self.__paused = False
        self.__task.start()
        if self.__timeout != None:
            self.end = time()+self.__timeout
            task(target=self.__clock).start()

    def pause(self):
        if self.__terminated or self.__paused:
            return
        self.__paused = True
        self.__task.pause()
        collect()

    def resume(self):
        if self.__terminated or not self.__paused:
            return
        self.__paused = False
        self.__task.resume()

    def terminate(self):
        if self.__terminated:
            return
        self.__paused = False
        self.__terminated = True
        self.__task.resume()
        self.__task.terminate()
        collect()

    @property
    def __status__(self):
        return {'paused': self.__paused, 'terminated': self.__terminated, 'ended': not self.__terminated and not self.__task.is_alive() and not self.__paused}

    @property
    def __priority__(self):
        return self.__priority

    @property
    def __result__(self):
        return self.__task.__result__

    @property
    def __task__id__(self):
        return self.__task.__task_id__

    def __str__(self) -> str:
        return str(self.__task)
