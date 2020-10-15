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
