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

  void Image::line(int _sx, int _sy, int _ex, int _ey, unsigned char _r, unsigned char _g, unsigned char _b, unsigned char _a  ) 
  {
    line(_sx,_sy,_ex,_ey,RGBA{_r,_g,_b,_a});
  }
  void Image::line(int _sx, int _sy, int _ex, int _ey, const RGBA &_p ) 
  {
    // make local copies of the inputs to match the algorithm on wikipedia
    int x0=_sx;
    int x1=_ex;
    int y0=_sy;
    int y1=_ey;

    int dx=std::abs(x1-x0);
    int sx = (x0<x1) ? 1 : -1;
    int dy = -abs(y1-y0);
    int sy = y0 < y1 ? 1 : -1;
    int err = dx+dy;
    while(true)
    {
      setPixel(x0,y0,_p);
      if (x0==x1 && y0==y1) 
      {
        break;
      }
      int e2 = 2*err;
      if (e2 >= dy) 
      {
            err += dy;
            x0 += sx;
      }
        if (e2 <= dx)
        {
            err += dx;
            y0 += sy;
        }
      }
// from https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
// plotLine(int x0, int y0, int x1, int y1)
//     dx =  abs(x1-x0);
//     sx = x0<x1 ? 1 : -1;
//     dy = -abs(y1-y0);
//     sy = y0<y1 ? 1 : -1;
//     err = dx+dy;  /* error value e_xy */
//     while (true)   /* loop */
//         plot(x0, y0);
//         if (x0==x1 && y0==y1) break;
//         e2 = 2*err;
//         if (e2 >= dy) /* e_xy+e_x > 0 */
//             err += dy;
//             x0 += sx;
//         end if
//         if (e2 <= dx) /* e_xy+e_y < 0 */
//             err += dx;
//             y0 += sy;
//         end if
//     end while
}
void Image::rectangle(int _tx, int _ty, int _bx, int _by, unsigned char _r, unsigned char _g, unsigned char _b, unsigned char _a ) 
{
  rectangle(_tx,_ty,_bx,_by,RGBA{_r,_g,_b,_a});
}
void Image::rectangle(int _tx, int _ty, int _bx, int _by, const RGBA &_p ) 
{
  // this really needs error checking and make sure that _tx > _ex etc.
  // TODO check dimensions and swap if required.
  for (int y=_ty; y<_by; ++y)
  {
    for(int x=_tx; x<_bx; ++x)
    {
      setPixel(x,y,_p);
    }
  }

}



