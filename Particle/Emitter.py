from Particle import Particle
from Vec3 import Vec3
from Random import Random
import random


class Emitter:
    def __init__(self, pos, num_particles):
        self._position = pos
        self._num_particles = num_particles
        self._particles = []
        self._init_particles()

    def _init_particles(self):
        for _ in range(self.num_particles):
            particle = self._create_particle()
            self._particles.append(particle)

    def _create_particle(self) -> Particle:
        EMIT_DIR = Vec3(0, 1, 0)
        SPREAD = 15
        direction = (
            EMIT_DIR * Random.random_positive_float()
            + Random.random_vector_on_sphere() * SPREAD
        )
        direction.y = abs(direction.y)
        max_life = random.randint(10, 50)
        colour = Random.random_positive_vec3()
        pos = self._position
        particle = Particle(
            pos=pos, dir=direction, colour=colour, life=0, max_life=max_life, scale=0.1
        )
        return particle

    def update(self, dt=0.1):
        GRAVITY = Vec3(0, -9.81, 0)
        for i, particle in enumerate(self._particles):
            particle.dir += GRAVITY * dt * 0.5
            particle.pos += particle.dir
            particle.life += 1
            particle.scale += 0.1
            if particle.life > particle.max_life:
                self._particles[i] = self._create_particle()

    def write_geo(self, file_name: str) -> None:
        with open(file_name, "w") as file:
            file.write("PGEOMETRY V5 \n")
            file.write(f"NPoints {len(self._particles)} NPrims 1 \n")
            file.write("NPointGroups 0 NPrimGroups 0\n")
            file.write("NPointAttrib 2 NVertexAttrib 0 NPrimAttrib 1 NAttrib 0\n")
            file.write("PointAttrib \n")
            file.write("Cd 3 float 1 1 1 \n")
            file.write("pscale 1 float 0.5 \n")
            for p in self._particles:
                file.write(f"{p.pos.x} {p.pos.y} {p.pos.z} 1 (")
                file.write(f"{p.colour.x} {p.colour.y} {p.colour.z} {p.scale} ) \n")
            file.write("PrimAttrib \n")
            file.write("generator 1 index 1 papi \n")
            file.write(f"Part {len(self._particles)} ")
            index_values = [i for i in range(len(self._particles))]
            file.write(" ".join(map(str, index_values)))
            file.write(" [0]  \n")
            file.write("beginExtra\n")
            file.write("endExtra \n")

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
