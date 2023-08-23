#include "work_space/LIE/include/pthread_minus_minus.hpp"
#include <string.h>
#include <stdio.h>
#include <iostream>
using namespace std;
// for this two, you are in responsible to insert to the correct place. IDK where is your thread executing once started and you want to do something to it.
// t_wait(condition);
// t_term(condition);

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
    if (t2->__get_res() == nullptr)
    {
        cout << "null" << endl;
    }
    else
    {
        cout << *(int *)(t2->__get_res()) << endl;
    }
}
