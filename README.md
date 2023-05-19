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
setattr(a, "onfinishtimeout", 5)# this arrt is discard
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
