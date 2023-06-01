from threading import Thread, Event
from sys import settrace
from gc import collect


class task(Thread):
    def __init__(self, *args, **keywords) -> None:
        Thread.__init__(self, *args, **keywords)

        # for blocking
        self.__pause_event = Event()

        # pause and terminate flag
        self.__pause_flag = False
        self.__terminate_flag = False

    # start func running
    def start(self) -> None:
        self.__run_backup = self.run
        self.run = self.__run
        Thread.start(self)

    def __run(self) -> None:
        settrace(self.__globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    # global trace
    def __globaltrace(self, frame, event, arg) -> None:
        # when get called
        if event == 'call':
            return self.__localtrace
        else:
            return None

    # local trace
    def __localtrace(self, frame, event, arg) -> None:
        # when need to pause the thread
        if self.__pause_flag:
            if event == 'line':
                # block the thread wait for event
                self.__pause_event.wait()

        if self.__terminate_flag:
            if event == 'line':
                # terminate the thread
                raise SystemExit()
        return self.__localtrace

    def pause(self) -> None:
        self.__pause_flag = True

    def resume(self) -> None:
        self.__pause_flag = False
        self.__pause_event.set()

    def terminate(self) -> None:
        self.__terminate_flag = True

    def is_terminated(self) -> bool:
        return self.__terminate_flag

    @classmethod
    def __collect__() -> None:
        collect()
