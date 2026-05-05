import pytest

from Particle import Particle
from Vec3 import Vec3


def test_particle_construct():
    p = Particle()
    assert p.pos == Vec3()
    assert p.dir == Vec3()
    assert p.colour == Vec3()
    assert p.life == 0
    assert p.max_life == 100
    assert p.scale == 2.0


def test_particle_values():
    pos = Vec3(1, 2, 3)
    dir = Vec3(4, 5, 6)
    colour = Vec3(7, 8, 9)
    max_life = 10
    life = 5
    scale = 3.0
    p = Particle(pos, dir, colour, life, max_life, scale)
    assert p.pos == pos
    assert p.dir == dir
    assert p.colour == colour
    assert p.max_life == max_life
    assert p.life == life
    assert p.scale == scale
