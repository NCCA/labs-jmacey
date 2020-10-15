#ifndef IMAGE_H_
#define IMAGE_H_

#include <cstdint>
#include <iostream>
struct RGBA
{
    union
    {
        uint32_t pixel=0;
        struct
        {
            unsigned char r;
            unsigned char g;
            unsigned char b;
            unsigned char a;
        };

    };
    RGBA()=default;
    RGBA(const RGBA &)=default;
    ~RGBA()=default;
    RGBA(unsigned char _r, unsigned char _g, unsigned char _b, unsigned char _a) :
    r{_r},g{_g},b{_b},a{_a} {}

    void print() const
    {
        std::cout << pixel <<' '<<static_cast<int>(r)<<' '<<static_cast<int>(g)<<' '<<' '<<static_cast<int>(b)<<' '<<static_cast<int>(a)<<'\n';
    }

};




#endif
