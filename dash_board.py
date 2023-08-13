from DS import heap


class dash_board:
    def __init__(self, heap_size=33) -> None:
        self.__heap = heap(heap_size)
        self.__ref = []
        self.__discard = self.__heap.__zero__-1
        self.__executable = 1

    def new_task(self, priority=0, time_out=None, group=None, target=None, name=None,
                 args=(), kwargs={}, daemon=False):
        pass

    def __next(self):
        pass

    def get_task(self):
        pass

    def remove_task(self):
        pass
