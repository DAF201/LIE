# LIE
Labor Is Evil

First thing first, I cannot guarentee everything happens properly like result ready, priority working properly, and thread pauses/resume/termeintes immidiently. Every functions are suggestion based.

Just provide some features like pause, resume, terminate, timeout, priority and return value to thread

I want to keep everything separate still, so I may use 'task' separately if i just need a pausable/resumable and terminatable thread at some point in the future

# features

Dash_board: provide priority and management

Clock: provide timeout

Task: provide pause, resume, terminate, and return value to thread

# note
1. clock is not inheritance from task, it is more like task class with more features
2. clock can terminate paused task, task cannot, you need to resume the task before terminate it otherwise it will stucked there
3. everything is suggestioned based! ordering, timing, resulting are not guarenteed
4. calling dash_board.terminate will exit exit the main thread 

# Example code
```python
from time import sleep
from task import task
from clock import clock
from dash_board import dash_board


def inf(name):
    while (True):
        print(name+'running')
        sleep(1)


def add(a, b):
    return a+b


d = dash_board(queue_size=1)
d.new_task(priority=4, time_out=2, target=inf, args=['first',])
d.new_task(priority=1, time_out=4, target=inf, args=['second',])
id = d.new_task(priority=6, target=add, args=[1, 2,])
sleep(3)
print(d.__get_result__(id))


tk = task(target=inf, args=['task'])
tkr = task(target=add, args=[4, 5])
tk.start()
tkr.start()
sleep(2)
tk.pause()
print(tkr.__result__)
sleep(2)
tk.resume()
sleep(2)
tk.terminate()

cl = clock(task(target=inf, args=['clock']), timeout=3)
clr = clock(task(target=add, args=[6, 7]))
cl.start()
clr.start()
sleep(2)
print(clr.__result__)

d.terminate()
```

```
firstrunning
secondrunning
firstrunning
secondrunning
secondrunning
3
taskrunning
secondrunning
taskrunning
9
taskrunning
taskrunning
clockrunning
clockrunning
clockrunning13

PS C:\Users\daf20\Documents\GitHub>
```
