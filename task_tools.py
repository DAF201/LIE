from sys import settrace
from gc import collect
from threading import Thread, Event
from datetime import datetime
from typing import Any
from functools import wraps
from concurrent import futures
from datetime import datetime, timedelta


def function_timer(seconds):
    """this only work for non-class function"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            # execute function
            future = futures.ThreadPoolExecutor(1).submit(func, *args, **kw)
            # set timeout exception
            future.set_exception(BaseException)
            # return result
            return future.result(timeout=seconds)
        return wrapper
    return decorator
