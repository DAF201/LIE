from threading import Thread
from config import *
from types import FunctionType, BuiltinFunctionType, NoneType
from priority import priority
from error_and_exception import TYPE_ERROR, raise_exception
from inspect import currentframe, isclass


class task:
    def __init__(self,
                 task_id: str | int,
                 task_content: FunctionType | BuiltinFunctionType | object,
                 task_params: list | None = None,
                 task_priority: int = 0,
                 **kwargs: dict) -> None:

        # type checking
        # id is str or int
        if type(task_id) not in [str, int]:
            raise_exception(TYPE_ERROR, currentframe(),
                            kwargs={"variable": "task.task_id"})
        # body can only be object(to run __init__) or function
        if type(task_content) not in [FunctionType, BuiltinFunctionType] and not isclass(task_content):
            raise_exception(TYPE_ERROR, currentframe(),
                            kwargs={"variable": "task.task_content"})
        # params can either be None or a list
        if type(task_params) not in [list, NoneType]:
            raise_exception(TYPE_ERROR, currentframe(),
                            kwargs={"variable": "task.task_params"})
        if type(task_priority) != int:
            raise_exception(TYPE_ERROR, currentframe(),
                            kwargs={"variable": "task.task_priority"})

        # all keyword args
        self.kwargs = kwargs
        kwargs_keys = self.kwargs.keys()

        # task id
        self.task_id = task_id

        # task function or object
        self.task_content = task_content

        # parameters
        self.task_params = task_params

        # priority of task, from 0-3
        #  0: not important task, can be delayed
        #  1: somehow important task, can start earlier than 0 task
        #  2: important, require a start_with_in range
        #  3: need to be started immediately, put at front of all other tasks

        if task_priority == 2:
            # default immediately start unless there is a 3 task at front
            start_with_in = self.kwargs['start_with_in'] if 'start_with_in' in self.kwargs.keys(
            ) else 0
            self.priority = priority(
                task_priority, start_with_in=start_with_in)

        # task need to be finished with in x secs?
        self.time_out = self.kwargs['time_out'] if 'time_out' in kwargs_keys else None
        # when task didn't finished with in x secs, do something?
        self.on_timeout = self.kwargs['on_timeout']if 'on_timeout' in kwargs_keys else None

        # task need to be repeated?
        self.repeat_times = self.kwargs['repeat_times'] if 'repeat_times' in kwargs_keys else None
        # interval between each repeat?
        self.repeat_interval = self.kwargs['repeat_interval'] if 'repeat_interval' in kwargs_keys else None

        # hooks
        self.on_create = self.kwargs['on_create'] if 'on_create' in kwargs_keys else None
        self.on_start = self.kwargs['on_start']if 'on_start' in kwargs_keys else None
        self.on_finish = self.kwargs['on_finish']if 'on_finish' in kwargs_keys else None
        self.on_remove = self.kwargs['on_remove']if 'on_remove' in kwargs_keys else None

    def __str__(self) -> str:
        task_body = self.task_content.__name__ if (type(self.task_content) in [
                                                   BuiltinFunctionType, FunctionType]) else self.task_content.__class__.__name__
        return """
                id: %s
                task: %s 
                params: %s
                kwargs: %s
                """ % (self.id, task_body, str(self.params), str(self.kwargs))


# task(1, None)
task(2, Thread, task_priority='1')
