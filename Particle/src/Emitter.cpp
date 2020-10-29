#include "Emitter.h"
#include "Random.h"
#include <iostream>

Emitter::Emitter(const Vec3 &_pos, size_t _numParticles)
{
  m_pos=_pos;
  m_numParticles=_numParticles;
  m_particles.resize(_numParticles);
  for(auto &p : m_particles)
  {
    resetParticle(p);
  }
}

void Emitter::update(float _deltaT)
{
 // std::cout<<"update "<<_deltaT<<'\n';
  Vec3 gravity(0.0f,-9.81f,0.0f);
  for(auto &p : m_particles)
  {
    p.dir += gravity * _deltaT *0.5f;
    p.pos += p.dir * _deltaT;
    p.scale += Random::randomPositiveFloat(0.05f);
    if(++p.life >=p.maxLife || p.pos.m_y <= 0.0f )
    {
      resetParticle(p);
    }
    std::cout<<p.pos.m_x<<' '<<p.pos.m_y<<' '<<p.pos.m_z<<'\n';
  }

}
void Emitter::saveFrame(int _frameNo)
{
  std::cout<<"save "<<_frameNo<<'\n';
}

void Emitter::resetParticle(Particle &io_p)
{
  io_p.pos=m_pos;
  io_p.dir = m_emitDir * Random::randomPositiveFloat() + Random::randomVectorOnSphere()*m_spread;
  io_p.dir.m_y = std::abs(io_p.dir.m_y);
  io_p.colour = Random::randomPositiveVec3();
  io_p.maxLife = static_cast<int>(Random::randomPositiveFloat(5000));
  io_p.life=0;
  io_p.scale=0.01f;
}





