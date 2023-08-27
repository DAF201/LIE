#ifndef class_minus_minus
#define class_minus_minus
#include <map>
#include <string>
#include <vector>
typedef void *(*func)(void *);
#define func_info(arg) (void *)arg, #arg
#define attr_info(arg) &arg, #arg
#define get_func(obj, key) (func)(*obj)[#key]
#define get_attr(obj, key, type) *(type *)(*obj)[#key]
#define set_func(obj, attr) (*obj)(func_info(attr))
#define set_attr(obj, attr) (*obj)(attr_info(attr))
class virtual_class
{
protected:
    static std::map<std::string, void *> attributes;
    std::string id = std::to_string((unsigned long long)(void **)this);
    std::string class_name = "virtual_class";

public:
    virtual_class()
    {
        this->class_name = __func__;
    }
    virtual void operator()(void *attr, std::string key)
    {
        this->attributes[this->id + key] = attr;
    }
    virtual void *operator[](std::string key)
    {
        return this->attributes[this->id + key];
    }
    virtual std::vector<void *> operator=(virtual_class *obj)
    {
        std::vector<void *> buffer = std::vector<void *>();
        for (std::map<std::string, void *>::iterator it = this->attributes.begin(); it != this->attributes.end(); ++it)
        {
            if ((it->first).rfind(this->id) == 0)
            {
                buffer.push_back(this->attributes[it->first]);
                this->attributes.erase(it->first);
            }
        }
        this->id = obj->id;
        return buffer;
    }
    virtual bool operator==(virtual_class *obj)
    {
        if (obj == this)
        {
            return true;
        }
        return false;
    }
    virtual std::string name()
    {
        return typeid(this).name();
    }
    virtual ~virtual_class()
    {
    }
};

std::map<std::string, void *> virtual_class::attributes = std::map<std::string, void *>();
#endif
