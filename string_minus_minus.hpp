// disclaimer: I have never test this yet

#ifndef string_minus_minus
#define string_minus_minus
#include <string>
#include <map>
#include <unordered_map>
#include <iostream>
#include <type_traits>

#define SALT "shio"                                                               // "salt" in JP
#define EMP_HASH -121758991                                                       // empty string hash with salt
#define print(arg) std::cout << arg << std::endl                                  // same my life
#define type_check(type_1, type_2) constexpr(std::is_same<type_1, type_2>::value) // check if two types are the same
static const std::string __emp = "";                                              // static empty string to init
static const std::string *__emp_ptr = &__emp;                                     // static empty string pointer pointing for init

typedef struct v_str_rec // saved in map
{
    int len = 0;                                  // size of this string
    int instances = 0;                            // how many instances are using this string, if it is down to zero it may be cleaned
    std::string *data = (std::string *)__emp_ptr; // empty string pointer
} str_dict;

class elastic_string : std::string
{
private:
    static std::map<int, v_str_rec *> dict; // static map to store all the existing strings
    static std::hash<std::string> hashing;  // hasher
    static int hash_str(std::string &);     // class method
    str_dict *this_str;                     // pointer of this string, pointing to somewhere on the map

public:
    elastic_string(std::string str) // create a new string or pointing to an existing string
    {
        if (str.compare("") == 0) // empty string
        {
            if (this->dict.count(EMP_HASH) == 1) // empty string record exist already
            {
                this->dict[EMP_HASH]->instances++;
            }
            else // create new record
            {
                v_str_rec *new_rec = new v_str_rec(); // to avoid being auto deleted
                new_rec->instances = 1;
                this->dict[EMP_HASH] = new_rec;
            }
            this->this_str = this->dict[EMP_HASH]; // hash key for empty string is fixed
            return;
        }

        // otherwise, not empty, calculate key

        int hash_key = elastic_string::hash_str(str);

        if (this->dict.count(hash_key) == 0) // record not exist, create one
        {
            v_str_rec *new_rec = new v_str_rec();
            std::string *new_str = new std::string(str);
            new_rec->data = new_str;
            new_rec->instances = 1;
            new_rec->len = new_str->size();
            this->dict[hash_key] = new_rec;
        }
        this->this_str = this->dict[hash_key]; // point to the struct in map
    }

    std::string *str()
    {
        return this->this_str->data; // fetch the string from current string pointer
    }

    const char *c_str()
    {
        return this->this_str->data->c_str();
    }

    int size()
    {
        return this->this_str->len;
    }

    template <typename string_like>
    void operator=(string_like str)
    {
        if type_check (string_like, elastic_string)
        {
            this->dict[elastic_string::hash_str(this.str())]->instances--; // reduce old instance
            this->this_str = str.this_str;                                 // copy pointer
            this->dict[elastic_string::hash_str(this.str())]->instances++; // increase new instance
        }
        else
        {
            // TODO
        }
    }

    template <typename string_like>
    std::string operator+(string_like str)
    {
        if type_check (string_like, elastic_string) // type check if they are the same
        {
            return *(this->this_str->data) + *(str.this_str->data);
        }
        else
        {
            return *(this->this_str->data) + str;
        }
    }

    template <typename string_like>
    void operator+=(string_like str)
    {
        std::string *buffer = new std::string();

        if type_check (string_like, elastic_string)
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
            this->dict[hash_key]->instances++; // new instance + 1
            delete buffer;                     // remove buffer as it is now needed any more
        }
        else
        {
            v_str_rec *new_rec = new v_str_rec(); // new record
            new_rec->data = buffer;               // save values
            new_rec->instances = 1;
            new_rec->len = buffer->size();
            this->dict[hash_key] = new_rec;
        }

        this->this_str = this->dict[hash_key];                                         // point to the new instance
        this->dict[elastic_string::hash_str(*(this->this_str->data))]->instances -= 1; // old instance - 1
    }
    static void clean(); // remove all no instant str from map
};

std::map<int, v_str_rec *> elastic_string::dict = std::map<int, v_str_rec *>();
std::hash<std::string> elastic_string::hashing = std::hash<std::string>();
int elastic_string::hash_str(std::string &str)
{
    return hashing(str + SALT); // add salt
}
#endif
