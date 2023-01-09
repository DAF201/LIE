from inspect import getframeinfo
from types import FrameType


def raise_exception(exception: Exception, frame: FrameType, **kwargs) -> None:
    (file, current_line, func_name,
     lines, index) = getframeinfo(frame)
    raise exception(kwargs=kwargs, file=file,
                    line=current_line, func=func_name)


class TYPE_ERROR(Exception):
    def __init__(self, *args: object, **kwargs: dict) -> None:
        super().__init__("incompatible variable typing at \n@file: %s\n@line: %s\n@function:%s\n@%s" %
                         (kwargs['file'], kwargs['line'], kwargs['func'], kwargs['kwargs']))


class TIME_OUT_ERROR(Exception):
    def __init__(self, *args: object, **kwargs) -> None:
        super().__init__()
