from Particle import Particle


class Emitter:
    def __init__(self, pos, num_particles):
        self._position = pos
        self._num_particles = num_particles
        self._particles = []
        self._init_particles()

    def _init_particles(self):
        for _ in range(self.num_particles):
            particle = Particle()
            self._particles.append(particle)

    @property
    def position(self):
        return self._position

    @property
    def num_particles(self):
        return self._num_particles

    @property
    def particles(self):
        return self._particles

    def render(self):
        for p in self._particles:
            print(p)
