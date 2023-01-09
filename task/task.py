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
                task_priority, start_with_in)

        self.time_out = self.kwargs['time_out'] if 'time_out' in kwargs_keys else None
        self.repeat_times = self.kwargs['repeat_times'] if 'repeat_times' in kwargs_keys else None
        self.repeat_interval = self.kwargs['repeat_interval'] if 'repeat_interval' in kwargs_keys else None

        self.on_create = self.kwargs['on_create'] if 'on_create' in kwargs_keys else None
        self.start_processing = self.kwargs['start_processing']if 'start_processing' in kwargs_keys else None
        self.finish_processing = self.kwargs['finish_processing']if 'finish_processing' in kwargs_keys else None
        self.on_remove = self.kwargs['on_remove']if 'on_remove' in kwargs_keys else None
        self.on_timeout = self.kwargs['on_timeout']if 'on_timeout' in kwargs_keys else None

    def __str__(self) -> str:
        if (type(self.task_content) in [BuiltinFunctionType, FunctionType]):
            return """
                id: %s
                function: %s 
                params: %s
                time out: %s
                interval: %s
                kwargs: %s
                """ % (self.id, self.task_content.__name__, str(self.params), str(self.time_out), str(self.interval), str(self.kwargs))
        else:
            return """
                id: %s
                object: %s 
                params: %s
                time out: %s
                interval: %s
                kwargs: %s
                """ % (self.id, self.task_content.__class__.__name__, str(self.params), str(self.time_out), str(self.interval), str(self.kwargs))


t = task("test", None, None, 1, on_timeout=print)
print(t.on_timeout)
print(t)
