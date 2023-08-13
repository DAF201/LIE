I want to keep everything separate still, so I may use 'task' separately if i just need a pausable/resumable and terminatable thread at some point in the future
# test
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
