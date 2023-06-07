from task_tools import *


class task(Thread):
    num_of_thread_running = 0

    def __init__(self, priority=0, end_callback=None, return_able=False, group=None, target=None, name=None,
                 args=(), kwargs={}, daemon=False) -> None:
        """priority from -2 to 2, end callback will be called after finished"""
        Thread.__init__(self, group=group, target=target, name=name,
                        args=args, kwargs=kwargs, daemon=daemon)
        self._return = None

        # for blocking
        self.__pause_event = Event()

        # pause and terminate flag
        self.__pause_flag = False
        self.__terminate_flag = False

        # task id for trace
        self.task_id = hash(self.getName()+str(args)+str(kwargs))
        self.priority = priority
        self.end_callback = end_callback
        self.return_able = return_able

        Thread.run = self.__result_run

    def start(self) -> None:
        self.__run_backup = self.run
        self.run = self.__run
        Thread.start(self)

    def __result_run(self):
        """over ride the Thread.run"""
        try:
            if self._target is not None:
                self._return = self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs

    def __run(self) -> None:
        """trace the thread to stop when need"""
        settrace(self.__globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    # global trace
    def __globaltrace(self, frame, event, arg) -> None:
        # when get called
        if event == 'call':
            # get local trace
            return self.__localtrace
        else:
            return None

    # local trace
    def __localtrace(self, frame, event, arg) -> None:
        # when need to pause/stop the thread
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

    def is_paused(self) -> bool:
        return self.__pause_flag

    def is_running(self) -> bool:
        return self.is_alive() and (not self.__pause_flag) and (not self.__terminate_flag)

    def __get_result__(self) -> Any:
        """cannot guarentee finished, will add a flag later but my lunch time is about to end"""
        return self._return
