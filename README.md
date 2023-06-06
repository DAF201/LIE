# timer testing
```python
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
