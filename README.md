# LIE
~~for C or C++ on linux environment~~

for linux C++ only, I gave up C part it is too annoying, and I can't guarentee it will work because when you try to pause/terminate it, the thread may passed the pausing/breaking point already and will not execute that part anymore.

Now the thread will not start once created, you need to call start to start the thread.

Also providing get result, pause, resume, and terminate.

## how to use
```c++
// function need to be in form of, param is basically a void* but I typedef it for easier reading
t_ret demo(cond_var &condition, param args)
// insert this into a suitable place of pausing a function
t_wait(condition);
// insert this into a suitable place of stopping a function
t_term(condition);
```
also I cannot guarentee when if the result is ready or not, if not it will return a nullptr

test.cpp
```c++
#include "work_space/LIE/include/pthread_minus_minus.hpp"
#include <string.h>
#include <stdio.h>
#include <iostream>
using namespace std;

t_ret demo1(cond_var &condition, param args)
{
    while (1)
    {
        t_wait(condition);
        t_term(condition);
        cout << *(int *)args << endl;
        sleep(1);
    }
    return args;
}
t_ret demo2(cond_var &condition, param args)
{
    t_wait(condition);
    return args;
}
int main()
{
    int str = 123;
    task *t1 = new task(demo1, &str);
    t1->__start();
    sleep(2);
    t1->__pause();
    sleep(2);
    t1->__resume();
    sleep(2);
    t1->__term();
    task *t2 = new task(demo2, &str);
    t2->__start();
    sleep(2);

    // this is not guarenteed to return the value, if the thread is still running it will reutrn a nullptr
    if (t2->__get_res() == nullptr)
    {
        cout << "null" << endl;
    }
    else
    {
        cout << *(int *)(t2->__get_res()) << endl;
    }
}
```
