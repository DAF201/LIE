// #include "work_space/LIE/include/pthread_minus_minus.hpp"
// #include <string.h>
// #include <stdio.h>
// #include <iostream>
// using namespace std;
// // for this two, you are in responsible to insert to the correct place. IDK where is your thread executing once started and you want to do something to it.
// // t_wait(condition);
// // t_term(condition);

// t_ret demo1(cond_var &condition, param args)
// {
//     while (1)
//     {
//         t_wait(condition);
//         t_term(condition);
//         cout << *(int *)args << endl;
//         sleep(1);
//     }
//     return args;
// }
// t_ret demo2(cond_var &condition, param args)
// {
//     t_wait(condition);
//     return args;
// }
// int main()
// {
//     int str = 123;
//     task *t1 = new task(demo1, &str);
//     t1->__start();
//     sleep(2);
//     t1->__pause();
//     sleep(2);
//     t1->__resume();
//     sleep(2);
//     t1->__term();
//     task *t2 = new task(demo2, &str);
//     t2->__start();
//     sleep(2);
//     if (t2->__get_res() == nullptr)
//     {
//         cout << "null" << endl;
//     }
//     else
//     {
//         cout << *(int *)(t2->__get_res()) << endl;
//     }
// }

// #include "work_space/LIE/include/class_minus_minus.hpp"
// #include <iostream>
// using namespace std;
// #include <stdarg.h>

// void *test(void *args)
// {
//     cout << *(string *)args << endl;
//     return nullptr;
// }
// class test_class : public virtual_class
// {
// };
// int main()
// {
//     test_class *a = new test_class();
//     set_func(a, test);
//     func b = get_func(a, test);
//     string str = "123";
//     b(&str);
//     int test_attr = 1;
//     set_attr(a, test_attr);
//     cout << get_attr(a, test_attr, int) << endl;
//     return 0;
// }


// #include "work_space/LIE/include/string_minus_minus.h"
// #include <iostream>
// using namespace std;
// int main()
// {
//     elastic_string *es = new elastic_string("test");
//     elastic_string *es2 = new elastic_string("test");
//     cout << es->str() << " " << es2->str() << endl;
//     *es += "";
//     cout << es->str() << " " << es2->str() << endl;
//     *es += "1";
//     cout << es->str() << " " << es2->str() << endl;
//     *es2 += "1";
//     cout << es->str() << " " << es2->str() << endl;
// }
