// disclaimer: I have never test this yet, and also unfinished

#ifndef string_minus_minus
#define string_minus_minus
#include <string>
#include <map>
#include <unordered_map>
#include <iostream>
#include <type_traits>
#define SALT "shio"
#define EMP_HASH -121758991
#define print(arg) std::cout << arg << std::endl
static const std::string __emp = "";
static const std::string *__emp_ptr = &__emp;

typedef struct v_str_dict
{
    int len = 0;
    int instances = 0;
    std::string *data = (std::string *)__emp_ptr;
} str_dict;

class elastic_string : std::string
{
private:
    static std::map<int, v_str_dict *> dict;
    static std::hash<std::string> hashing;
    static int hash_str(std::string &);
    str_dict *this_str;

public:
    elastic_string(std::string str) // create a new string or pointing to an existing string
    {
        if (str.compare("") == 0) // empty string
        {
            if (this->dict.count(EMP_HASH) == 1) // empty string record exist already
            {
                this->dict[EMP_HASH]->instances += 1;
            }
            else // create new record
            {
                v_str_dict *new_rec = new v_str_dict();
                new_rec->instances = 1;
                this->dict[EMP_HASH] = new_rec;
            }
            this->this_str = this->dict[EMP_HASH];
            return;
        }

        int hash_key = elastic_string::hash_str(str);

        if (this->dict.count(hash_key) == 1)
        {
            this->this_str = this->dict[hash_key];
            return;
        }
        else
        {
            v_str_dict *new_rec = new v_str_dict();
            std::string *new_str = new std::string(str);
            new_rec->data = new_str;
            new_rec->instances = 1;
            new_rec->len = new_str->size();
            this->dict[hash_key] = new_rec;
            this->this_str = new_rec;
            return;
        }
    }

    std::string *str()
    {
        return this->this_str->data; // fetch the string from current string pointer
    }

    virtual std::string operator+(std::string &str)
    {
        return *(this->this_str->data) + str;
    }

    template <typename string_like>
    void operator+=(string_like str)
    {
        std::string *buffer = new std::string();

        if constexpr (std::is_same<string_like, elastic_string>::value) // type check
        {
            if (str.this_str->data == __emp_ptr) // is es, check empty string
            {
                return;
            }
            *buffer = *(str.this_str->data);
        }
        else
        {
            *buffer = str;
            if (buffer->compare("") == 0) // test empty string case
            {
                return;
            }
        }

        *buffer = *(this->this_str->data) + *buffer;      // concat string
        int hash_key = elastic_string::hash_str(*buffer); // create hash key

        if (this->dict.count(hash_key) == 1) // the concat string already exist
        {
            this->dict[hash_key]->instances += 1; // new instance + 1
            delete buffer;                        // remove buffer as it is now needed any more
        }
        else
        {
            v_str_dict *new_rec = new v_str_dict(); // new record
            new_rec->data = buffer;                 // save values
            new_rec->instances = 1;
            new_rec->len = buffer->size();
            this->dict[hash_key] = new_rec;
        }

        this->this_str = this->dict[hash_key];                                         // point to the new instance
        this->dict[elastic_string::hash_str(*(this->this_str->data))]->instances -= 1; // old instance - 1
    }
    static void clean(); // remove all no instant str from map
};

std::map<int, v_str_dict *> elastic_string::dict = std::map<int, v_str_dict *>();
std::hash<std::string> elastic_string::hashing = std::hash<std::string>();
int elastic_string::hash_str(std::string &str)
{
    return hashing(str + SALT); // add salt
}
#endif
