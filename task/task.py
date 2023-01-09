from typing import Any
from types import FunctionType, BuiltinFunctionType
from priority import priority


class task:
    def __init__(self,
                 id: str | int,
                 task_content: FunctionType | BuiltinFunctionType | object | None,
                 params: list | Any | None,
                 task_priority: int = 0,
                 **kwargs: dict) -> None:

        # all keyword args
        self.kwargs = kwargs
        kwargs_keys = self.kwargs.keys()

        # task id
        self.id = str(id)

        # task function or object
        self.task_content = task_content

        # parameters
        self.params = params

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
