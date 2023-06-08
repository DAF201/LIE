from task_tools import Thread, Event, settrace, Any

# this class is good now, add feature to other classes


class task(Thread):
    num_of_thread_created = 0
    num_of_thread_running = 0

    def __init__(self, priority=0,  return_able=False, time_out=None, group=None, target=None, name=None,
                 args=(), kwargs={}, daemon=False) -> None:
        """priority from -2 to 2, end callback will be called after finished"""
        self.num_of_thread_created += 1

        Thread.__init__(self, group=group, target=target, name=name,
                        args=args, kwargs=kwargs, daemon=daemon)

        # for blocking
        self.__pause_event = Event()

        # pause and terminate flag
        self.__pause_flag = True
        self.__terminate_flag = False

        # task id for trace
        self.task_id = hash(self.getName()+str(args)+str(kwargs))
        self.priority = priority
        self.return_able = return_able
        self.time_out = time_out
        if return_able:
            self._return = None

        Thread.run = self.__result_run

    def start(self) -> None:
        self.__pause_flag = False
        self.__run_backup = self.run
        self.run = self.__run
        self.num_of_thread_running += 1
        Thread.start(self)

    def __result_run(self):
        """over ride the Thread.run"""
        try:
            if self._target is not None:
                if self.return_able:
                    self._return = self._target(*self._args, **self._kwargs)
                else:
                    self._target(*self._args, **self._kwargs)
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
        if self.is_running:
            self.num_of_thread_running -= 1
            self.__pause_flag = True

    def resume(self) -> None:
        if self.__pause_flag and self.is_alive() and (not self.__terminate_flag):
            self.num_of_thread_running += 1
            self.__pause_flag = False
            self.__pause_event.set()

    def terminate(self) -> None:
        if not self.__terminate_flag:
            self.num_of_thread_running -= 1
            self.__terminate_flag = True

    def is_terminated(self) -> bool:
        return self.__terminate_flag

    def is_paused(self) -> bool:
        return self.__pause_flag

    def is_running(self) -> bool:
        return self.is_alive() and (not self.__pause_flag) and (not self.__terminate_flag)

    def is_ended(self) -> bool:
        return not self.is_alive() and (not self.__pause_flag) and (not self.__terminate_flag)

    def __get_result__(self) -> Any:
        """cannot guarentee finished, will add a flag later but my lunch time is about to end"""
        if self.return_able:
            self.join()
            return self._return
        return None

    def __del__(self):
        self.num_of_thread_created -= 1
