#include <iostream>
#include <cstdlib>
#include "Image.h"
int main()
{
  std::cout<<"Image\n";
  Image a;
  a.setPixel(200,200,255,255,255,255);
  return  EXIT_SUCCESS;
}
