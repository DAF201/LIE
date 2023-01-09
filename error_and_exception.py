from inspect import getframeinfo


def raise_exception(exception, frame):
    (file, current_line, func_name,
     lines, index) = getframeinfo(frame)
    raise exception(file=file, line=current_line, func=func_name)


class TYPE_ERROR(Exception):
    def __init__(self, *args: object, **kwargs) -> None:
        super().__init__("incompatible variable typing at \n@file: %s\n@line: %s\n@function:%s" %
                         (kwargs['file'], kwargs['line'], kwargs['func']))
