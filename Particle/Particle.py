from dataclasses import dataclass, field

from Vec3 import Vec3


@dataclass
class Particle:
    pos: Vec3 = field(default_factory=Vec3)
    dir: Vec3 = field(default_factory=Vec3)
    colour: Vec3 = field(default_factory=Vec3)
    life: int = 0
    max_life: int = 100
    scale: float = 2.0

    def __str__(self):
        return f"{self.pos},{self.scale}"
