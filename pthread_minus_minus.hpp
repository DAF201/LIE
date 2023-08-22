#ifndef PTHREAD_MINUS
#define PTHREAD_MINUS
#include <unistd.h>
#include <pthread.h>
#include <stdio.h>
#include <signal.h>
#define lock pthread_mutex_t
#define cond pthread_cond_t
#define t_wait(conditional)                              \
    {                                                    \
        if (condition.p != 0)                            \
            pthread_cond_wait(condition.c, condition.l); \
    }
struct __cond_var
{
    lock *l;
    cond *c;
    int p;
};
typedef __cond_var cond_var;
typedef void *(*func)(cond_var &, void *);
typedef void *param;

class task
{
public:
    task(func subroutine, param args)
    {

        this->subroutine = subroutine;
        this->args[0] = args;
        this->private_condition.l = &(this->private_lock);
        this->private_condition.c = &(this->private_cond);
        this->private_condition.p = 0;
        pthread_create(
            &(this->tid), NULL, [](void *self) -> void *
            {static_cast<task *>(self)->__exec();return nullptr; },
            this);
    }
    int __start()
    {
        return pthread_cond_signal(&(this->private_cond));
    }
    int __exec()
    {
        // pause the function, wait for the start()
        pthread_cond_wait(&(this->private_cond), &(this->private_lock));
        this->subroutine(this->private_condition, this->args);
        return 0;
    }
    void __resume()
    {
        this->private_condition.p = 0;
        pthread_cond_signal(&(this->private_cond));
    }
    void __pause()
    {
        this->private_condition.p = 1;
    }

private:
    func subroutine;
    param args[2];
    pthread_t tid;
    pthread_mutex_t private_lock = PTHREAD_MUTEX_INITIALIZER;
    pthread_cond_t private_cond = PTHREAD_COND_INITIALIZER;
    cond_var private_condition;
};
#endif
