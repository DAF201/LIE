# LIE
~~for C or C++ on linux environment~~

for C++ only, I gave up C part it is too annoying
```c++
// how to use:
// add this to where you think it is good okay to pause the thread while running
t_wait(condition);
//the function need to be like
void *func(cond_var &condition, void *args)
```
example function:
```c++
    string str = "t";
    task *t = new task(print, &str);
    t->__resume();
    t->__pause();
```
