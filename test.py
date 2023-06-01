# #Timer test
# import task_timer
# from threading import Thread


# def test():
#     for i in range(10000000000):
#         pass


# def t(t):
#     print("%s" % t)


# a = Thread(target=test)
# b = Thread(target=test)
# setattr(a, "onfinish", t)
# setattr(a, "onfinishargs", "123")
# setattr(a, "onfinishtimeout", 5)
# a.start()
# b.start()
# print(task_timer.TASK_TIMER_WAITLIST)
# task_timer.TASK_TIMER_WAITLIST.append(a)
# task_timer.TASK_TIMER_WAITLIST.append(b)
# print(task_timer.TASK_TIMER_WAITLIST)

# #Task body test
import task_body
import time
from datetime import datetime


def test_func():
    while True:
        time.sleep(0.25)
        print("test func running")


t = task_body.task(target=test_func)
t.start()

time.sleep(2)

print("pause test")
print("Current Time =", datetime.now().strftime("%H:%M:%S"))
try:
    t.pause()
    time.sleep(3)
except BaseException as e:
    print(e)

time.sleep(2)

print("resume test")
print("Current Time =", datetime.now().strftime("%H:%M:%S"))
t.resume()

time.sleep(2)

print("terminate test")
print("Current Time =", datetime.now().strftime("%H:%M:%S"))
try:
    t.terminate()
except BaseException as e:
    print(e)

t.join()
print("fully terminated")
print("Current Time =", datetime.now().strftime("%H:%M:%S"))
