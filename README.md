# timer testing
## this part is reworking
```python
# this part need to be rewrite to work with task container and task class

import task_timer
from threading import Thread
def test():
    for i in range(10000000000):
        pass
def t(t):
    print(t)
a = Thread(target=test)
b = Thread(target=test)
setattr(a, "onfinish", t)
setattr(a, "onfinishargs", "123")
setattr(a, "onfinishtimeout", 5)# this arrt is discard(I will go back to this later, I just figure how to)
a.start()
b.start()
print(task_timer.TASK_TIMER_WAITLIST)
task_timer.TASK_TIMER_WAITLIST.append(a)
task_timer.TASK_TIMER_WAITLIST.append(b)
print(task_timer.TASK_TIMER_WAITLIST)

```

```
EMPTY
EMPTY
EMPTY[]

EMPTY[<Thread(Thread-7 (test), started 8852)>, <Thread(Thread-8 (test), started 9580)>]

123
EMPTY
```

# pause, resume, and terminate test
```python
import task_body
from time import sleep
from datetime import datetime


def test_func():
    while True:
        sleep(0.25)
        print("test func running")


t = task_body.task(target=test_func)
t.start()
# to let the task run for a few sec
sleep(2)
# task paused
print("pause test")
print("Current Time =", datetime.now().strftime("%H:%M:%S"))
try:
    t.pause()
except BaseException as e:
    print(e)

# test if task is still running
sleep(2)

print("resume test")
print("Current Time =", datetime.now().strftime("%H:%M:%S"))
t.resume()

# test if task resumed
sleep(2)

print("terminate test")
print("Current Time =", datetime.now().strftime("%H:%M:%S"))
try:
    t.terminate()
except BaseException as e:
    print(e)

# block main wait for task to be terminate
t.join()
print("fully terminated")
print("Current Time =", datetime.now().strftime("%H:%M:%S"))

```

```
test func running
test func running
test func running
test func running
test func running
test func running
test func running
pause test
Current Time = 13:31:40
resume test
Current Time = 13:31:42
test func running
test func running
test func running
test func running
test func running
test func running
test func running
test func running
terminate test
Current Time = 13:31:44
fully terminated
Current Time = 13:31:44
```
# container and task result test

```python

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
# task get result test

t = task(target=max, args=(1, 2))
t.start()
t.join()
print(t.__get_result__())

```

```
4
None

-9215257271159047211
<task(Thread-7 (print), initial)>
<task(Thread-8 (sum), initial)>
<task(Thread-9 (any), initial)>

3
<task(Thread-7 (print), initial)>
2

<task(Thread-8 (sum), initial)>
<task(Thread-9 (any), initial)>

{'detached': [<task_container.ring object at 0x000002408ADE4DF0>, <task_container.stack object at 0x000002408ADE4640>, <task_container.queue object at 0x000002408ADE44C0>], -2: [<task_container.ring object at 0x000002408ADE4E50>, <task_container.stack object at 0x000002408ADE4760>, <task_container.queue object at 0x000002408ADE4550>], -1: [<task_container.ring object at 0x000002408ADE4430>, <task_container.stack object at 0x000002408ADE4610>, <task_container.queue object at 0x000002408ADE4310>], 0: [<task_container.ring object at 0x000002408DC44160>, <task_container.stack object at 0x000002408DC44A60>, <task_container.queue object at 0x000002408DC44B20>], 1: [<task_container.ring object at 0x000002408DC44BE0>, <task_container.stack object at 0x000002408DC44C40>, <task_container.queue object at 0x000002408DC44D00>], 2: [<task_container.ring object at 0x000002408DC44DC0>, <task_container.stack 
object at 0x000002408DC44E20>, <task_container.queue object at 0x000002408DC44EE0>]}

2
```
