from DS import heap
from task import task
from clock import clock
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

    def new_task(self, priority=1, time_out=None, inverval=1, group=None, target=None, name=None,
                 args=(), kwargs={}, daemon=False):
        new_task = task(group=group, target=target,
                        name=name, args=args, kwargs=kwargs, daemon=daemon)
        new_clock = clock(new_task, priority, time_out, inverval)
        self.__heap.insert(new_clock)

    def exec(self):
        self.__exect = task(target=self.exect)
        self.__exect.start()
        while (True):
            for c in self.__ref:
                c: clock
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

    @property
    def __ref__(self):
        return self.__ref
