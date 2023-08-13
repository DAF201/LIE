from LIE.DS import heap
from LIE.task import task
from LIE.clock import clock
from time import sleep
from gc import collect


class dash_board:
    def __init__(self, heap_size=33, queue_size=3) -> None:
        self.__queue_size = queue_size
        self.__heap = heap(heap_size)
        self.__ref = []*queue_size
        self.__active = 0
        self.__exec = task(target=self.exec)
        self.__exec.start()
        self.task_ref = {}

    def new_task(self, priority=1, time_out=None, inverval=1, group=None, target=None, name=None,
                 args=(), kwargs={}, daemon=False):
        new_task = task(group=group, target=target,
                        name=name, args=args, kwargs=kwargs, daemon=daemon)
        new_clock = clock(new_task, priority, time_out, inverval)
        self.__heap.insert(new_clock)
        self.task_ref[new_clock.__task__id__] = new_clock
        return new_clock.__task__id__

    def exec(self):
        self.__exect = task(target=self.exect)
        self.__exect.start()
        while (True):
            for c in self.__ref:
                if c.__status__['terminated'] or c.__status__['ended']:
                    self.__ref.remove(c)
                elif c.__status__['paused']:
                    self.__ref.remove(c)
                    self.__heap.insert(c)
                else:
                    sleep(1)

    def exect(self):
        while (True):
            if self.__active < self.__queue_size:
                if not self.__heap.__is_empty__:
                    self.__ref.append(self.__heap.pop())
                    for clock in self.__ref:
                        if clock.__status__['paused']:
                            clock.start()
                else:

                    sleep(1)

    def terminate(self):
        self.__exec.terminate()
        self.__exect.terminate()
        collect()
        raise SystemExit()

    def __get_result__(self, id):
        result = self.task_ref[id].__result__
        del self.task_ref[id]
        return result
