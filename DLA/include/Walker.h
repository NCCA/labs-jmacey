#ifndef WALKER_H_
#define WALKER_H_
#include <cstdlib>
#include <memory>
#include <random>
#include "Image.h"
class Walker
{
  public :
    Walker(size_t _w, size_t _h);
  private :
    std::unique_ptr<Image> m_map;
    std::uniform_int_distribution<> m_xRand;
    std::uniform_int_distribution<> m_yRand;


};

#endif
