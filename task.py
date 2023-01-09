from types import FunctionType, BuiltinFunctionType, NoneType
from task_priority import priority
from error_and_exception import TYPE_ERROR, raise_exception
from inspect import currentframe, isclass
from typing import Any
from gc import collect


class task:
    def __init__(self,
                 task_id: str | int,
                 task_content: FunctionType | BuiltinFunctionType | object,
                 task_params: list | None = None,
                 task_priority: int = 0,
                 **kwargs: dict) -> None:

        # type checking
        self.type_checking(task_id, task_content, task_params, task_priority)

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
        if task_priority >= 2:
            # default immediately start unless there is a 3 task at front
            start_with_in = self.kwargs['start_with_in'] if 'start_with_in' in self.kwargs.keys(
            ) else 0

        self.priority = priority(
            task_priority, start_with_in=start_with_in) if task_priority > 1 else priority(task_priority)

        # task need to be finished with in x secs?
        self.time_out = self.kwargs['time_out'] if 'time_out' in kwargs_keys else None
        # when task didn't finished with in x secs, do something?
        self.on_timeout = self.kwargs['on_timeout']if 'on_timeout' in kwargs_keys else None

        # task need to be repeated?
        self.repeat_times = self.kwargs['repeat_times'] if 'repeat_times' in kwargs_keys else None
        # interval between each repeat?
        self.repeat_interval = self.kwargs['repeat_interval'] if 'repeat_interval' in kwargs_keys else None
        # require a lock when running?
        self.locked = self.kwargs['repeat_interval'] if 'repeat_interval' in kwargs_keys else False

        # hooks
        self.on_create = self.kwargs['on_create'] if 'on_create' in kwargs_keys else None
        self.on_start = self.kwargs['on_start']if 'on_start' in kwargs_keys else None
        self.on_pause = self.kwargs['on_pause']if 'on_pause' in kwargs_keys else None
        self.on_resume = self.kwargs['on_resume']if 'on_resume' in kwargs_keys else None
        self.on_finish = self.kwargs['on_finish']if 'on_finish' in kwargs_keys else None
        self.on_remove = self.kwargs['on_remove']if 'on_remove' in kwargs_keys else None

        # Because this is init so on_create cannot return anything
        if self.on_create != None:
            self.on_create()

    # check types when init
    def type_checking(self, task_id, task_content, task_params, task_priority):
        # id is str or int
        if type(task_id) not in [str, int]:
            raise_exception(TYPE_ERROR, currentframe(),
                            kwargs={'variable': 'task.task_id'})
        # body can only be object(to run __init__) or function
        if type(task_content) not in [FunctionType, BuiltinFunctionType] and not isclass(task_content):
            raise_exception(TYPE_ERROR, currentframe(),
                            kwargs={'variable': 'task.task_content'})
        # params can either be None or a list
        if type(task_params) not in [list, NoneType]:
            raise_exception(TYPE_ERROR, currentframe(),
                            kwargs={'variable': 'task.task_params'})
        if type(task_priority) != int:
            raise_exception(TYPE_ERROR, currentframe(),
                            kwargs={'variable': 'task.task_priority'})

    # task compare
    def __eq__(self, __o: object) -> bool:
        try:
            return (self.task_id == __o.task_id) and (self.task_content == __o.task_content) and (self.task_params == __o.task_params)
        except:
            return False

    # task on start
    def __enter__(self) -> Any:
        if self.on_start != None:
            return self.on_start()

    # task on finish
    def __exit__(self, type: Any, value: Any, trace: Any) -> Any:
        if self.on_finish != None:
            return self.on_finish()

    # print
    def __str__(self) -> str:
        return """
                id: %s
                task: %s 
                params: %s
                kwargs: %s
                """ % (self.task_id, self.task_content, str(self.task_params), str(self.kwargs))

    # on remove
    def __del__(self):
        # on remove cannot be returned
        if self.on_remove != None:
            self.on_remove()
        collect()

    # Not used
    def __getattr__(self, name: Any) -> None:
        return None

    # Not used
    def __setattr__(self, name: Any, value: Any) -> None:
        return None
