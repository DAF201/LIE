from threading import Thread
from task_body import task
from functools import wraps
from concurrent import futures
from task_exceptions import task_timeout_exception, raise_timeout_exception
from datetime import datetime, timedelta
TASK_TIMER_WAITLIST = []


def function_timer(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            # execute function
            future = futures.ThreadPoolExecutor(1).submit(func, *args, **kw)
            # set timeout exception
            future.set_exception(task_timeout_exception)
            # return result
            return future.result(timeout=seconds)
        return wrapper
    return decorator


class task_timer:
    # all tasks being track
    __task_pool: list
    __task_pool_is_empty = True
    __task_pool_size = 0
    __task_pool_index = 0

    # main thread to add and track task
    __task_timer_main: Thread

    def __init__(self) -> None:
        self.__task_pool = []
        self.__task_timer_main = Thread(target=self.__start__)
        # self.__task_timer_main.daemon = True
        self.__task_timer_main.start()

    def __start__(self) -> None:
        while (True):
            try:
                # check if there is task to add
                self.__add_task__()

                # update pool
                self.__task_pool_is_empty = True if self.__task_pool_size == 0 else False

                # checking
                if (self.__task_pool_is_empty):
                    continue
                else:
                    # if index out boundary
                    if (self.__task_pool_index >= self.__task_pool_size-1):
                        self.__task_pool_index = 0

                    # check if a task is alive
                    cur_task: Thread
                    cur_task = self.__task_pool[self.__task_pool_index]
                    # dead
                    if (not cur_task.is_alive() or cur_task.__getattribute__("discard")):
                        self.__remove_task__(cur_task)

                    # check timeout
                    try:
                        if (datetime.now() - cur_task.__getattribute__("starttime")
                                > cur_task.__getattribute__("timeout")):
                            cur_task.__getattribute__(
                                "raise_timeout_exception")()
                    except task_timeout_exception as time_out_exception:
                        cur_task.__setattr__("discard", True)
                        cur_task.daemon = True
            except Exception as e:
                print(e)
            finally:
                # next thread in pool
                self.__task_pool_index += 1
                if (self.__task_pool_is_empty):
                    print("EMPTY")

    # add new task to pool
    def __add_task__(self) -> None:
        if (len(TASK_TIMER_WAITLIST) != 0):
            new_task: task
            new_task = TASK_TIMER_WAITLIST.pop(0)

            # set a thread is still being cared
            if (not hasattr(new_task, "discard")):
                setattr(new_task, "discard",
                        False)
            # set stopper
            if (not hasattr(new_task, "raise_timeout_exception")):
                setattr(new_task, "raise_timeout_exception",
                        raise_timeout_exception)
            # set start time
            if (not hasattr(new_task, "starttime")):
                setattr(new_task, "starttime", datetime.now())

            # set timeout if not set
            if (not hasattr(new_task, "timeout")):
                setattr(new_task, "timeout", timedelta(seconds=3))

            self.__task_pool.append(new_task)
            self.__task_pool_size += 1
        else:
            return

    # remove task
    def __remove_task__(self, target_task: Thread) -> Thread:
        try:
            # reduce pool size
            self.__task_pool_size -= 1
            # check if has a on finish callback
            if (hasattr(target_task, "onfinish") and hasattr(target_task, "onfinishargs")):
                target_task.__getattribute__(
                    "onfinish")(target_task.__getattribute__("onfinishargs"))
            return self.__task_pool.remove(target_task)
        except Exception as e:
            print(e)


TASK_TIMER = task_timer()
