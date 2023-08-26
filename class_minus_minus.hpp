#ifndef class_minus_minus
#define class_minus_minus
#include <map>
#include <string>
typedef void *(*func)(void *);
#define func_info(arg) (void *)arg, #arg
#define attr_info(arg) &arg, #arg
#define get_func(obj,key) (func)(*obj)[#key]
#define get_attr(obj,key,type) *(type*)(*obj)[#key] 
#define set_func(obj,attr) (*obj)(func_info(attr))
#define set_attr(obj,attr) (*obj)(attr_info(attr))
class virtual_class
{
protected:
    static std::map<std::string, void *> attributes;

public:
    void operator()(void *attr, std::string key)
    {
        this->attributes[key] = attr;
    }
    void *operator[](std::string key)
    {
        return this->attributes[key];
    }
};

std::map<std::string, void *> virtual_class::attributes = std::map<std::string, void *>();
#endif
