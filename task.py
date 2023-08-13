from threading import Thread, Event
from sys import settrace


class task(Thread):
    '''priority start from 1 to 1073741823(2^30-1), 0 reserved for dummy and 1073741823 reserved for heap 0 defadault. higher priority will be execute first'''

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, daemon=False) -> None:
        self.__args = args
        self.__kwargs = kwargs
        self.__target = target
        self.__task_id = self.__hash__()
        self.__pause_event = Event()
        self.__pause_flag = True
        self.__terminate_flag = False
        self._return = None
        Thread.__init__(self, group=group, target=target, name=name,
                        args=args, kwargs=kwargs, daemon=daemon)
        Thread.run = self.__result_run

    def start(self):
        self.__pause_flag = False
        self.__run_backup = self.run
        self.run = self.__run
        Thread.start(self)

    def pause(self):
        if self.__running__:
            self.__pause_flag = True

    def resume(self):
        if self.__pause_flag and self.is_alive() and (not self.__terminate_flag):
            self.__pause_flag = False
            self.__pause_event.set()

    def terminate(self):
        if not self.__terminate_flag:
            self.__terminate_flag = True

    # keep unique for each instance
    @staticmethod
    def __result_run(self):
        try:
            if self._target is not None:
                self._return = self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs

    def __run(self):
        settrace(self.__globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def __globaltrace(self, frame, event, arg):
        if event == 'call':
            return self.__localtrace
        else:
            return None

    def __localtrace(self, frame, event, arg):
        if self.__pause_flag:
            if event == 'line':
                self.__pause_event.wait()

        if self.__terminate_flag:
            if event == 'line':
                raise SystemExit()
        return self.__localtrace

    @property
    def __task_id__(self):
        return self.__task_id

    @property
    def __terminated__(self):
        return self.__terminate_flag

    @property
    def __paused__(self):
        return self.__pause_flag

    @property
    def __running__(self):
        return self.is_alive() and (not self.__pause_flag) and (not self.__terminate_flag)

    @property
    def __ended__(self):
        return not self.is_alive() and (not self.__pause_flag) and (not self.__terminate_flag)

    @property
    def __result__(self):
        return self._return

    def __hash__(self):
        return hash(str(self.__target)+str(self.__args)+str(self.__kwargs))

    def __str__(self):
        return str({'target': self.__target, 'id': self.__task_id, 'status': {'paused': self.__paused__, 'terminated': self.__terminated__, 'ended': self.__ended__}})
