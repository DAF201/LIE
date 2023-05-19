from threading import Thread
from datetime import datetime, timedelta


class clock:
    __start_time: datetime
    __current_time: datetime

    def clock(self, start_time: datetime):
        self.__start_time = start_time
        self.__current_time = datetime.now()
        self.__duration = timedelta(seconds=0)

    def time_delta(self) -> None:
        if (datetime.now()-self.__current_time > 1):
            raise Exception
