from config import *
from error_and_exception import TYPE_ERROR, raise_exception
from inspect import currentframe


class priority:
    def __init__(self, task_priority: int = 0, **kwargs) -> None:
        if type(task_priority) != int:
            raise_exception(TYPE_ERROR, currentframe(),
                            kwargs={'variable': 'priority.task_priority'})
        self.task_priority = task_priority

        if task_priority > 1 and kwargs != {}:
            if type(kwargs['start_with_in']) != int:
                raise_exception(TYPE_ERROR, currentframe(),
                                kwargs={'variable': 'priority.kwargs[\'start_with_in\']'})
            self.start_with_in = kwargs['start_with_in']
            self.kwargs = kwargs.pop('start_with_in')
        else:
            self.start_with_in = 0

    def __call__(self) -> int:
        return self.task_priority
