#ifndef IMAGE_H_
#define IMAGE_H_

#include <cstdint>
#include <iostream>
#include <string_view>
#include <memory>

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


class Image
{
public :
  Image()=default;
  Image(size_t _w, size_t _h);
  Image(size_t _w, size_t _h,unsigned char _r, unsigned char _g,
        unsigned char _b, unsigned char _a);
  size_t width() const;
  size_t height () const;
  RGBA getPixel(size_t _x, size_t y) const ;
  void clear(unsigned char _r, unsigned char _g, unsigned char _b, unsigned char _a=255);
  bool setPixel(size_t _x, size_t _y,unsigned char _r, unsigned char _g, unsigned char _b, unsigned char _a=255) ;
  bool setPixel(size_t _x, size_t _y,RGBA _p);
  bool save(const std::string_view _fname) const;
private :
  size_t m_width=0;
  size_t m_height=0;
  std::unique_ptr<RGBA []> m_pixels;
};





#endif
