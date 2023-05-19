from datetime import datetime
from typing import Any


class task_exception:
    __exception_info: str
    __exception_obj: object
    __exception_occur_time: datetime
    __exception_handle_time: datetime
    __exception_args: Any

    def __init__(self, obj, info, *args) -> None:
        # exception info to display
        self.__exception_info = info
        # which object caused exception
        self.__exception_obj = obj
        # occur time and handled time
        self.__exception_occur_time = datetime.now()
        self.__exception_handle_time = datetime.fromtimestamp(0)
        # other args
        self.__exception_args = args
        return


class task_timeout_exception(BaseException, task_exception):
    def __init__(self, *args: object) -> None:
        super().__init__("timeout")


class task_runtime_exception(task_exception):
    def __init__(self):
        return


class task_type_exception(task_exception):
    def __init__(self):
        return


def raise_timeout_exception():
    # raise task_timeout_exception
    raise task_timeout_exception
