#include "Emitter.h"
#include "Random.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <fmt/format.h>

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
   // std::cout<<p.pos.m_x<<' '<<p.pos.m_y<<' '<<p.pos.m_z<<'\n';
  }

}
void Emitter::saveFrame(int _frameNo)
{
  std::cout<<"save "<<_frameNo<<'\n';
  std::ofstream file;
  file.open(fmt::format("particle{:04d}.geo",_frameNo+1));
  std::stringstream ss;
  ss << "PGEOMETRY V5\n";
  ss << "NPoints "<< m_numParticles << " NPrims 1 \n";
  ss << "NPointGroups 0 NPrimGroups 0 \n";
  ss << "NPointAttrib 2 NVertexAttrib 0 NPrimAttrib 1 NAttrib 0\n";

  ss <<"PointAttrib \n";
  ss <<"Cd 3 float 1 1 1 \n";
  ss <<"pscale 1 float 1 \n";

  for(auto p : m_particles)
  {
    ss<<p.pos.m_x<<' '<<p.pos.m_y<<' '<<p.pos.m_z<<" 1 (";
    ss<<p.colour.m_x<<' '<<p.colour.m_y<<' '<<p.colour.m_z<<' '<<p.scale<<")\n";
  }
  ss<<"PrimitiveAttrib\n";
  ss<<"generator 1 index 1 papi \n";
  ss<<"Part "<<m_numParticles<<' ';

  for(size_t i=0; i<m_numParticles; ++i)
    {
      ss<<i<<' ';
    }
  ss <<"[0]\n";
  ss<<"beginExtra\n";
  ss<<"endExtra\n";
  file<<ss.rdbuf();
  file.close();
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





