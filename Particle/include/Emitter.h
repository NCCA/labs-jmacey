#ifndef EMITTER_H_
#define EMITTER_H_
#include <cstdlib>
#include "Vec3.h"
#include <vector>
#include "Particle.h"

class Emitter
{
public :
  Emitter(const Vec3 &_pos, size_t _numParticles);
  ~Emitter()=default;
  void update(float _deltaT);
  void saveFrame(int _frameNo);
private :
    void resetParticle(Particle &io_p);
    Vec3 m_pos;
    float m_spread = 1.5f;
    Vec3 m_emitDir = Vec3(0.0f,10.0f,0.0f);
    size_t m_numParticles=1000;
    std::vector<Particle> m_particles;
};

#endif
