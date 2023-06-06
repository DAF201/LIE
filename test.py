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
# import task_body
# from time import sleep
# from datetime import datetime


# def test_func():
#     while True:
#         sleep(0.25)
#         print("test func running")


# t = task_body.task(target=test_func)
# t.start()
# # to let the task run for a few sec
# sleep(2)
# # task paused
# print("pause test")
# print("Current Time =", datetime.now().strftime("%H:%M:%S"))
# try:
#     t.pause()
# except BaseException as e:
#     print(e)

# # test if task is still running
# sleep(2)

# print("resume test")
# print("Current Time =", datetime.now().strftime("%H:%M:%S"))
# t.resume()

# # test if task resumed
# sleep(2)

# print("terminate test")
# print("Current Time =", datetime.now().strftime("%H:%M:%S"))
# try:
#     t.terminate()
# except BaseException as e:
#     print(e)

# # block main wait for task to be terminate
# t.join()
# print("fully terminated")
# print("Current Time =", datetime.now().strftime("%H:%M:%S"))

# Container test

from task_body import *
from task_container import *
from task_body import task
r = ring()

r.append(1)
r.append(2)
r.append(3)
r.append("ds")

r[3] = 4
print(r[3])
print(r[5])
print()
# this will not stop so I am not testing it here

# for x in r:
#     print(x)
# print(r.length)

t1 = task(target=print)
t2 = task(target=sum)
t3 = task(target=any)
print(t1.task_id)

lnl = linked_node_list()
lnl.append(t1)
lnl.append(t2)
lnl.append(t3)
for tasks in lnl:
    print(tasks)
print()
print(len(lnl))
print(lnl.remove(0))
print(len(lnl))
print()
for tasks in lnl:
    print(tasks)

print()
tc = task_container()
print(tc)
print()
# task get cleresult test

t = task(target=max, args=(1, 2))
t.start()
t.join()
print(t.__get_result__())
