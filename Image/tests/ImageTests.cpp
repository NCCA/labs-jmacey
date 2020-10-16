#include <gtest/gtest.h>
#include "Image.h"

TEST(RGBA,construct)
{
    RGBA pixel;
    ASSERT_TRUE(pixel.r == 0);
    ASSERT_TRUE(pixel.g == 0);
    ASSERT_TRUE(pixel.b == 0);
    ASSERT_TRUE(pixel.a == 0);

}

TEST(RGBA,userCtor)
{
    RGBA pixel(255,100,22,128);
    ASSERT_EQ(pixel.r,255);
    ASSERT_EQ(pixel.g,100);
    ASSERT_EQ(pixel.b,22);
    ASSERT_EQ(pixel.a,128);
}

TEST(RGBA,copy)
{
    RGBA p1(1,2,3,4);
    auto p2=p1;
    ASSERT_TRUE(p1.r == p2.r);
    ASSERT_TRUE(p1.g == p2.g);
    ASSERT_TRUE(p1.b == p2.b);
    ASSERT_TRUE(p1.a == p2.a);
}

TEST(IMAGE,defaultCtor)
{
  Image a;
  ASSERT_EQ(a.width(),0);
  ASSERT_EQ(a.height(),0);
}


TEST(IMAGE,userCtor)
{
  Image a(1024,720);
  ASSERT_EQ(a.width(),1024);
  ASSERT_EQ(a.height(),720);
}


TEST(IMAGE,getPixelDefault)
{
  Image a(20,20);
  for(size_t y=0; y<a.height(); ++y)
  {
    for(size_t x=0; x<a.width(); ++x)
    {
      auto p = a.getPixel(x,y);
      EXPECT_EQ(p.r,0);
      EXPECT_EQ(p.g,0);
      EXPECT_EQ(p.b,0);
      EXPECT_EQ(p.a,0);
    }
  }
}



TEST(IMAGE,getPixelUser)
{
  Image a(20,20,255,128,55,255);
  for(size_t y=0; y<a.height(); ++y)
  {
    for(size_t x=0; x<a.width(); ++x)
    {
      auto p = a.getPixel(x,y);
      EXPECT_EQ(p.r,255);
      EXPECT_EQ(p.g,128);
      EXPECT_EQ(p.b,55);
      EXPECT_EQ(p.a,255);
    }
  }
}



TEST(IMAGE,clear)
{
  Image a(20,20);
  for(size_t y=0; y<a.height(); ++y)
  {
    for(size_t x=0; x<a.width(); ++x)
    {
      auto p = a.getPixel(x,y);
      EXPECT_EQ(p.r,0);
      EXPECT_EQ(p.g,0);
      EXPECT_EQ(p.b,0);
      EXPECT_EQ(p.a,0);
    }
  }
  a.clear(12,128,255,57);
  for(size_t y=0; y<a.height(); ++y)
  {
    for(size_t x=0; x<a.width(); ++x)
    {
      auto p = a.getPixel(x,y);
      EXPECT_EQ(p.r,12);
      EXPECT_EQ(p.g,128);
      EXPECT_EQ(p.b,255);
      EXPECT_EQ(p.a,57);
    }
  }
}


TEST(IMAGE,setPixel)
{
  Image a(20,20);
  EXPECT_TRUE(a.setPixel(2,5,255,128,55,255));
  auto p=a.getPixel(2,5);
  EXPECT_EQ(p.r,255);
  EXPECT_EQ(p.g,128);
  EXPECT_EQ(p.b,55);
  EXPECT_EQ(p.a,255);

  EXPECT_FALSE(a.setPixel(29342,5995,255,128,55,255));
}

TEST(IMAGE,setPixelRGBA)
{
  Image a(20,20);
  RGBA p{255,128,55,255};
  EXPECT_TRUE(a.setPixel(2,5,p));
  auto p1=a.getPixel(2,5);
  EXPECT_EQ(p1.r,255);
  EXPECT_EQ(p1.g,128);
  EXPECT_EQ(p1.b,55);
  EXPECT_EQ(p1.a,255);
  EXPECT_FALSE(a.setPixel(29342,5995,{255,128,55,255}));
}

TEST(IMAGE,save)
{
  Image a(200,200,255,0,0,255);
  EXPECT_TRUE(a.save("test.png"));
}



