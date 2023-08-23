#ifndef PTHREAD_MINUS
#define PTHREAD_MINUS
#include <unistd.h>
#include <pthread.h>
#include <signal.h>
#define t_wait(condition)                                      \
    {                                                          \
        if (condition.p != 0)                                  \
            pthread_cond_wait(&(condition.c), &(condition.l)); \
    }
#define t_term(condition)     \
    {                         \
        if (condition.t != 0) \
            return nullptr;   \
    }
typedef struct __cond_var
{
    pthread_mutex_t l;
    pthread_cond_t c;
    int p;
    int t;
} cond_var;
typedef void *param;
typedef void *t_ret;
typedef t_ret (*func)(cond_var &, param);
class task
{
public:
    task(func subroutine, param args)
    {
        this->subroutine = subroutine;
        this->args = args;
        this->private_condition.l = PTHREAD_MUTEX_INITIALIZER;
        this->private_condition.c = PTHREAD_COND_INITIALIZER;
        this->private_condition.p = 0;
        pthread_create(
            &(this->tid), NULL, [](void *self) -> void *
            {static_cast<task *>(self)->__exec();return nullptr; },
            this);
    }
    void __start()
    {
        sleep(1);
        this->private_condition.p = 0;
        pthread_cond_signal(&(this->private_condition.c));
    }
    void __exec()
    {
        pthread_cond_wait(&(this->private_condition.c), &(this->private_condition.l));
        this->result = this->subroutine(this->private_condition, this->args);
    }
    void __resume()
    {
        this->private_condition.p = 0;
        pthread_cond_signal(&(this->private_condition.c));
    }
    void __pause()
    {
        this->private_condition.p = 1;
    }
    void __term()
    {
        this->private_condition.t = 1;
    }
    t_ret __get_res()
    {
        return this->result;
    }
    ~task()
    {
        pthread_join(this->tid, nullptr);
    }

private:
    func subroutine;
    param args;
    t_ret result;
    pthread_t tid;
    cond_var private_condition;
};
#endif
