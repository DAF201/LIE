# test
```python
from task import task
from DS import heap
from time import sleep
from clock import clock


def fin():
    print('running')
    sleep(1)


def inf():
    while (True):
        print('1 is running')
        sleep(1)
        break


def inf2():
    while (True):
        print('2 is running')
        sleep(1)


def inf3():
    while (True):
        print('3 is running')
        sleep(1)


tk = task(target=fin)
tk1 = task(target=inf)
tk2 = task(target=inf2)
tk3 = task(target=inf3)
t = clock(tk)
t1 = clock(tk1, timeout=3, priority=2)
t2 = clock(tk2, timeout=6, priority=3)
t3 = clock(tk3)

t.start()
t1.start()
t2.start()
t3.start()

print(t.__status__)
print(t1.__status__)
print(t2.__status__)
print(t3.__status__)

sleep(3)

print(t.__status__)
print(t1.__status__)
print(t2.__status__)
print(t3.__status__)

sleep(4)

print(t.__status__)
print(t1.__status__)
print(t2.__status__)
print(t3.__status__)

t3.terminate()
print(t.__status__)
print(t1.__status__)
print(t2.__status__)
print(t3.__status__)
```
```
running2 is running1 is running


{'paused': False, 'terminated': False, 'ended': False}
3 is running
{'paused': False, 'terminated': False, 'ended': False}
{'paused': False, 'terminated': False, 'ended': False}
{'paused': False, 'terminated': False, 'ended': False}
2 is running
3 is running
2 is running
3 is running
{'paused': False, 'terminated': False, 'ended': True}
{'paused': False, 'terminated': False, 'ended': True}
{'paused': False, 'terminated': False, 'ended': False}
{'paused': False, 'terminated': False, 'ended': False}
2 is running
3 is running
2 is running
3 is running
2 is running
3 is running
2 is running
3 is running
{'paused': False, 'terminated': False, 'ended': True}
{'paused': False, 'terminated': True, 'ended': False}
{'paused': False, 'terminated': True, 'ended': False}
{'paused': False, 'terminated': False, 'ended': False}
{'paused': False, 'terminated': False, 'ended': True}
{'paused': False, 'terminated': True, 'ended': False}
{'paused': False, 'terminated': True, 'ended': False}
{'paused': False, 'terminated': True, 'ended': False}
PS C:\Users\daf20\Documents\GitHub>
```
