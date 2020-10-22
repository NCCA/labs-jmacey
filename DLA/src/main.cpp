#include <iostream>
#include <cstdlib>
#include "Walker.h"
#include <fmt/format.h>

int main()
{
  std::cout<<"DLA Simulation\n";
  Walker w(400,400);
  for(int i=0; i<100; ++i)
  w.randomImageSeed();

  int toWrite=0;
  int imageStep=10;

 for(int i=0; i<10000; ++i)
 {
  if(w.walk() == true)
  {
    if(!(++toWrite %imageStep))
    w.saveImage(fmt::format("image{:04d}.png",toWrite));
  }
  w.resetStart();
 }


  return EXIT_SUCCESS;
}
