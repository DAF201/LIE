from types import FunctionType, BuiltinFunctionType, NoneType
from task_priority import priority
from error_and_exception import *
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

        # raise exception if didn't pass type check
        if not self.type_checking(task_id, task_content, task_params, task_priority):
            # raise_exception(TASK_INIT_ERROR, currentframe(),
            #                 kwargs={})
            return

        self.kwargs = kwargs
        kwargs_keys = self.kwargs.keys()

        self.task_id = task_id  # string or int
        self.task_content = task_content  # function or object
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

        # need to be done within x sec?
        self.time_out = self.kwargs['time_out'] if 'time_out' in kwargs_keys else None

        # didn't finished with in x secs, do something?
        # function or object
        self.on_timeout = self.kwargs['on_timeout']if 'on_timeout' in kwargs_keys else None

        # task need to be repeated?
        self.repeat_times = self.kwargs['repeat_times'] if 'repeat_times' in kwargs_keys else None

        # interval between each repeat?
        self.repeat_interval = self.kwargs['repeat_interval'] if 'repeat_interval' in kwargs_keys else None

        # require a lock when running? (only for important tasks)
        self.locked = self.kwargs['repeat_interval'] if 'repeat_interval' in kwargs_keys else False

        # hooks
        self.on_create = self.kwargs['on_create'] if 'on_create' in kwargs_keys else None
        self.on_start = self.kwargs['on_start']if 'on_start' in kwargs_keys else None
        self.on_pause = self.kwargs['on_pause']if 'on_pause' in kwargs_keys else None
        self.on_resume = self.kwargs['on_resume']if 'on_resume' in kwargs_keys else None
        self.on_finish = self.kwargs['on_finish']if 'on_finish' in kwargs_keys else None
        self.on_remove = self.kwargs['on_remove']if 'on_remove' in kwargs_keys else None
        self.on_exception = self.kwargs['on_exception']if 'on_exception' in kwargs_keys else None

        # Because this is init so on_create cannot return anything
        if self.on_create != None:
            self.on_create()

    # check types when init
    def type_checking(self, task_id, task_content, task_params, task_priority) -> None:
        '''check if the task inited with correct data types'''
        # id is str or int
        if type(task_id) not in [str, int]:
            raise_exception(TYPE_ERROR, currentframe(),
                            kwargs={'variable': 'task.task_id', 'obj': self.__str__().replace('\n', '')})
        # body can only be object(to run __init__) or function
        if type(task_content) not in [FunctionType, BuiltinFunctionType] and not isclass(task_content):
            raise_exception(TYPE_ERROR, currentframe(),
                            kwargs={'variable': 'task.task_content', 'obj': self.__str__().replace('\n', '')})
        # params can either be None or a list
        if type(task_params) not in [list, NoneType]:
            raise_exception(TYPE_ERROR, currentframe(),
                            kwargs={'variable': 'task.task_params', 'obj': self.__str__().replace('\n', '')})
        if type(task_priority) != int:
            raise_exception(TYPE_ERROR, currentframe(),
                            kwargs={'variable': 'task.task_priority', 'obj': self.__str__().replace('\n', '')})
        return True

    # task compare
    # def __eq__(self, __o: object) -> bool:
    #     try:
    #         return (self.task_id == __o.task_id) and (self.task_content == __o.task_content) and (self.task_params == __o.task_params)
    #     except:
    #         return False

    # task on start

    def __enter__(self) -> Any:
        '''task on start'''
        try:
            if self.on_start != None:
                self.on_start()
        except Exception as e:
            print(e)
        finally:
            return self
    # task on finish

    def __exit__(self, type: Any, value: Any, trace: Any) -> Any:
        '''task on finish'''
        try:
            if self.on_finish != None:
                self.on_finish()
            return False
        except Exception as e:
            print(e)
            return True

    # printing
    def __str__(self) -> str:
        return '''id: %s
                task: %s 
                params: %s
                kwargs: %s
                ''' % (self.task_id, self.task_content, str(self.task_params), str(self.kwargs))

    # on remove
    def __del__(self):
        '''clean up'''
        # on remove cannot be returned
        try:
            if self.on_remove != None:
                self.on_remove()
        except Exception as e:
            print(e)
        finally:
            collect()

    # Not used
    def __getattr__(self, name: Any) -> None:
        '''avoid raise exception when try to get an undefined property'''
        return None

    # Not used
    def __setattr__(self, name: Any, value: Any) -> None:
        '''not allowed'''
        return None


a = task(1, 1)
