#include "Emitter.h"
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
  std::cout<<"update "<<_deltaT<<'\n';
}
void Emitter::saveFrame(int _frameNo)
{
  std::cout<<"save "<<_frameNo<<'\n';
}

void Emitter::resetParticle(Particle &io_p)
{
  io_p.pos=m_pos;
}



