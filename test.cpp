#include "work_space/LIE/include/pthread_minus_minus.hpp"
#include <string.h>
#include <stdio.h>
#include <iostream>
using namespace std;

void *print(cond_var &condition, void *str)
{
    cout << *((string *)str) << endl;
    while (1)
    {
        t_wait(condition);
        cout << "running" << endl;
        sleep(1);
    }
    return nullptr;
}

int main()
{
    signal(SIGTSTP, SIG_IGN);
    string str = "t";
    task *t = new task(print, &str);
    sleep(3);
    t->__resume();
    sleep(3);
    t->__pause();
    sleep(3);
    t->__resume();
    sleep(3);
}
