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
    void randomImageSeed();
    void saveImage(const std::string &_fname) const;
    void resetStart();
    bool walk();
  private :
    void initRNG();
    std::unique_ptr<Image> m_map;
    std::uniform_int_distribution<> m_xRand;
    std::uniform_int_distribution<> m_yRand;
    int m_xpos;
    int m_ypos;


};

#endif
