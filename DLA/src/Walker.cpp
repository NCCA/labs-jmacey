#include "Walker.h"

#include <random>

std::random_device g_rd;
std::seed_seq g_seed{g_rd(), g_rd(), g_rd(), g_rd(), g_rd(), g_rd(), g_rd(), g_rd()};
std::mt19937 g_rng(g_seed);
std::uniform_int_distribution<>g_walkDir(-1,1);


Walker::Walker(size_t _w, size_t _h)
{
  m_map =  std::make_unique<Image>(_w,_h,255,255,255,0);
  initRNG();
  resetStart();
}

void Walker::initRNG()
{
  // we will select a point inside the image so we don't check edges
  // this is a bit of an optimisation
  m_xRand=std::uniform_int_distribution<>(1,m_map->width()-1);
  m_yRand=std::uniform_int_distribution<>(1,m_map->height()-1);
}

void Walker::randomImageSeed()
{
  m_map->setPixel(m_xRand(g_rng),m_yRand(g_rng),0,0,0,255);
}

void Walker::saveImage(const std::string &_fname) const
{
   m_map->save(_fname);
}

void Walker::resetStart()
{
  m_xpos=m_xRand(g_rng);
  m_ypos=m_yRand(g_rng);
  std::cout<<"New Start "<< m_xpos<<' '<<m_ypos<<'\n';

}

bool Walker::walk()
{
  // indicate im walking
  bool walking =true;
  // return if found
  bool found;
  while(walking)
  {
    //move walker
    m_xpos += g_walkDir(g_rng);
    m_ypos += g_walkDir(g_rng);
    // see if we move off image
    if(m_xpos ==0 || m_xpos >= m_map->width()-1 ||
       m_ypos ==0 || m_ypos >= m_map->height()-1)
      {
        walking =false;
        found = false;
        break;
      }
    // see if we have a hit
    for(int y=-1; y<=1; ++y)
    {
     for(int x=-1; x<=1; ++x)
     {
       // sample pixel
       auto p=m_map->getPixel(m_xpos+x,m_ypos+y);
       if(p.a == 255)
       {
         std::cout<<"found position\n";
         m_map->setPixel(m_xpos,m_ypos,0,0,0,255);
         walking = false;
         found = true;
       }
     }
    }
  }
  return found;
}








