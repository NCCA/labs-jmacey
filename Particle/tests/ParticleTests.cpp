#include <gtest/gtest.h>
#include "Particle.h"
#include "Emitter.h"
TEST(Particle,ctor)
{
  Particle p;
  ASSERT_FLOAT_EQ(p.pos.m_x,0.0f);
  ASSERT_FLOAT_EQ(p.pos.m_y,0.0f);
  ASSERT_FLOAT_EQ(p.pos.m_z,0.0f);

  ASSERT_FLOAT_EQ(p.dir.m_x,0.0f);
  ASSERT_FLOAT_EQ(p.dir.m_y,0.0f);
  ASSERT_FLOAT_EQ(p.dir.m_z,0.0f);

  ASSERT_FLOAT_EQ(p.colour.m_x,0.0f);
  ASSERT_FLOAT_EQ(p.colour.m_y,0.0f);
  ASSERT_FLOAT_EQ(p.colour.m_z,0.0f);

  ASSERT_EQ(p.life,0);
  ASSERT_EQ(p.maxLife,0);
  ASSERT_FLOAT_EQ(p.scale,0.01f);

}

TEST(Vec3,userCtor)
{
  Vec3 v(0.1f,0.2f,0.3f);
  EXPECT_FLOAT_EQ(v.m_x,0.1f);
  EXPECT_FLOAT_EQ(v.m_y,0.2f);
  EXPECT_FLOAT_EQ(v.m_z,0.3f);

}


TEST(Emitter,ctor)
{
  Emitter e(Vec3(0,0,0),100);
}







