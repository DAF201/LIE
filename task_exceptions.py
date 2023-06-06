from task_tools import *
from task_timer import TASK_TIMER


class task_exception:
    __exception_info: str
    __exception_obj: object
    __exception_occur_time: datetime
    __exception_handle_time: datetime
    __exception_args: Any

    # flag if need to stop the task when exception occur
    __if_stop_task = False
    # if need to take any future action
    __exception_handler = None

    def __init__(self, obj, *args) -> None:
        # exception info to display
        self.__exception_info = ""
        # which object caused exception
        self.__exception_obj = obj
        # occur time and handled time
        self.__exception_occur_time = datetime.now()
        self.__exception_handle_time = datetime.fromtimestamp(0)
        # other args
        self.__exception_args = args

    def __message__(self) -> None:
        """display the message of the exception"""
        print("@%s\tMessage: %s\tFrom:%s" %
              (self.__exception_occur_time, self.__exception_info, self.__exception_obj))
        if (self.__exception_args != None):
            print(self.__exception_args)

    def __str__(self) -> None:
        self.__message__()


class task_timeout_exception(BaseException, task_exception):
    def __init__(self, *args: object) -> None:
        """args: 1. Message 2. if want to stop the task 3.function to take"""
        super().__init__("timeout")
        # max args: 3 or no reaction needed
        if (len(args) > 3 or len(args) == 0):
            return
        if (len(args) == 1):
            self.__exception_info = args[0]
        elif (len(args) == 2):
            self.__exception_info = args[0]
            self.__if_stop_task = args[1]
        else:
            self.__exception_info = args[0]
            self.__if_stop_task = args[1]
            self.__exception_handler = args[2]

        if (self.__if_stop_task):
            try:
                if (self.__exception_handler != None):
                    self.__exception_handler()
                TASK_TIMER.__remove_task__(self.__exception_obj)
            except Exception as e:
                print(e)
            finally:
                self.__exception_handle_time = datetime.now()
                print("timeout exception of %s being handled/discarded @%s" %
                      (self.__exception_obj, self.__exception_handle_time))

    def __str__(self) -> str:
        return super().__str__()


class task_runtime_exception(task_exception, BaseException):
    # what kind of exception occured
    __exception_type = BaseException

    def __init__(self, obj, *args) -> None:
        super().__init__(obj, *args)


class task_type_exception(task_exception, BaseException):
    """wrong type args being passed in to task/timer/TASKMGR"""

    def __init__(self, obj, info, *args) -> None:
        super().__init__(obj, info, *args)


def raise_timeout_exception():
    """debug use, throw a timeout exception to discard a task?"""
    # raise task_timeout_exception
    raise task_timeout_exception


def raise_timeout_exception(obj: object, *args):
    raise task_timeout_exception
