# LIE
labor is evil x 

linear insertion enquiry ✓

Just provide some features like pause, resume, terminate, timeout, priority and return value to thread

I want to keep everything separate still, so I may use 'task' separately if i just need a pausable/resumable and terminatable thread at some point in the future
# dash board
the priority is not guarenteed, it cannot guarentee higher priority task being executed first
```python
from dash_board import dash_board
from time import sleep


def fiv(name):
    sleep(5)
    print(name+'finished')


d = dash_board(queue_size=1)
d.new_task(priority=1, target=fiv, args=['first'])
sleep(1)
d.new_task(priority=2, target=fiv, args=['sec'])
sleep(1)
d.new_task(priority=3, target=fiv, args=['third'])
d.new_task(priority=4, target=fiv, args=['fourth'])

sleep(6)
print(d.__ref__)
d.terminate()
```

```
firstfinished
secfinished
fourthfinished
thirdfinished
[]
```
# Clcok
```python
from task import task
from time import sleep
from clock import clock


def fin():
    print('running')
    sleep(1)

def inf(i):
    while (True):
        print('%s is running\n' % str(i))
        sleep(1)

tk = task(target=fin)
tki = task(target=inf, args=[1,])
tkit = task(target=inf, args=['tkit',])

c1 = clock(tk)
c2 = clock(tki, timeout=2)
c3 = clock(tkit)
c1.start()
c2.start()
c3.start()

sleep(3)
print(c1.__status__)
print(c2.__status__)
print(c3.__status__)
sleep(3)
c3.terminate()
print(c1.__status__)
print(c2.__status__)
print(c3.__status__)

```
```
1 is running
running

tkit is running

tkit is running
1 is running


1 is running
tkit is running


{'paused': False, 'terminated': False, 'ended': True}
{'paused': False, 'terminated': True, 'ended': False}
{'paused': False, 'terminated': False, 'ended': False}
tkit is running

tkit is running

tkit is running

{'paused': False, 'terminated': False, 'ended': True}
{'paused': False, 'terminated': True, 'ended': False}
{'paused': False, 'terminated': True, 'ended': False}
```
# return value
if result ready is not guarenteed, you need to check clock.__status__['ended']
```python
from dash_board import dash_board
from time import sleep
from task import task
from clock import clock


def fiv(name):
    sleep(5)
    print(name+'finished')


def add(a, b):
    sleep(1)
    return a+b


tk = task(target=add, args=[1, 2,])
t = clock(tk)
t.start()
sleep(2)
print(t.__result__)
d = dash_board(queue_size=1)
id = d.new_task(priority=1, target=add, args=[1, 1,])
sleep(2)
print(d.__get_result__(id))
print(d.task_ref)
d.terminate()

```
```
3
2
{}
```
