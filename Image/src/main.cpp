#include <iostream>
#include <cstdlib>
#include "Image.h"
#include <random>

constexpr size_t width = 800;
constexpr size_t height = 800;

int main()
{
  std::cout<<"Image\n";
  Image a(width,height,255,255,255,255);
  std::mt19937 rng;
  std::uniform_int_distribution<>pointx(0,width);
  std::uniform_int_distribution<>pointy(0,height);
  std::uniform_int_distribution<unsigned char>colour(0,255);

  for(int i=0; i<2000; ++i)
  {
    a.line(pointx(rng),pointy(rng),pointx(rng),pointy(rng),{colour(rng),colour(rng),colour(rng),255});
  }
  a.save("lines.png");
  a.clear(255,255,255,255);
  for(int i=0; i<2000; ++i)
  {
    a.rectangle(pointx(rng),pointy(rng),pointx(rng),pointy(rng),{colour(rng),colour(rng),colour(rng),255});
  }
  a.save("rect.png");


  return  EXIT_SUCCESS;
}
