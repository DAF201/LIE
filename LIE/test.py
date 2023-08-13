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
