#include "Image.h"
#include <OpenImageIO/imageio.h>

size_t Image::width() const
{
  return m_width;
}
size_t Image::height () const
{
  return m_height;
}

Image::Image(size_t _w, size_t _h) : m_width{_w}, m_height{_h}
{
  m_pixels = std::make_unique<RGBA []>(_w*_h);
}

Image::Image(size_t _w, size_t _h,unsigned char _r, unsigned char _g,
             unsigned char _b, unsigned char _a) : m_width{_w}, m_height{_h}
{
  m_pixels = std::make_unique<RGBA []>(_w*_h);
  RGBA p{_r,_g,_b,_a};
  for(size_t i=0; i<_w*_h; ++i)
    m_pixels[i]=p;

}


RGBA Image::getPixel(size_t _x, size_t _y) const
{
  return m_pixels[m_width*_y + _x];
}

void Image::clear(unsigned char _r, unsigned char _g, unsigned char _b, unsigned char _a)
{
  RGBA p{_r,_g,_b,_a};
  for(size_t i=0; i<m_width*m_height; ++i)
  {
    m_pixels[i]=p;
  }
}


bool Image::setPixel(size_t _x, size_t _y,unsigned char _r, unsigned char _g, unsigned char _b, unsigned char _a)
{
  if(_x >m_width || _y>m_height)
  {
    return false;
  }
  RGBA p{_r,_g,_b,_a};
  m_pixels[m_width*_y + _x]=p;
  return true;
}


bool Image::setPixel(size_t _x, size_t _y, RGBA _p)
{
  if(_x >m_width || _y>m_height)
  {
    return false;
  }
  m_pixels[m_width*_y + _x]=_p;
  return true;
}

bool Image::save(std::string_view _fname) const
{
  bool success=true;

  using namespace OIIO;
  auto out = ImageOutput::create (_fname.data());
  if(!out)
  {
    return false;
  }
  ImageSpec spec(m_width,m_height,4, TypeDesc::UINT8);
  success=out->open(_fname.data(),spec);
  success=out->write_image(TypeDesc::UINT8,m_pixels.get());
  success=out->close();
  return success;
}


