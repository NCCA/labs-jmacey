from OpenGL.GL.AMD.depth_clamp_separate import GL_FALSE
from typing import Tuple

import numpy as np
from ncca.ngl import Vec3

GRAVITY = np.array((0.0, -9.81, 0.0), dtype=np.float32)


class Emitter:
    def __init__(
        self, position: Vec3, num_particles: int, max_alive: int, max_per_frame: int, life_range: Tuple[int, int]
    ):
        self._position = position
        self.max_per_frame = max_per_frame
        self.life_range = life_range
        self.max_alive = max_alive
        self._num_particles = num_particles
        self.position = np.zeros((self._num_particles, 3), dtype=np.float32)  # x,y,z * num_part
        self.colour = np.zeros((self._num_particles, 3), dtype=np.float32)  # r,g,b
        self.direction = np.zeros((self._num_particles, 3), dtype=np.float32)  # x,y,z
        self.life = np.zeros((self._num_particles), dtype=int)
        self.max_life = np.zeros((self._num_particles), dtype=int)
        self.alive = np.full(self._num_particles, False, dtype=np.bool)
        self._init_particles()

    def update(self, dt):
        self.direction += GRAVITY * (dt * 0.5)
        self.position += self.direction
        self.life += 1

        if np.count_nonzero(self.alive) <= self.max_alive:
            num_to_create = np.random.randint(0, self.max_per_frame)
            dead_indices = np.where(self.alive == False)[0]
            revive_indices = dead_indices[:num_to_create]
            self.alive[revive_indices] = True

        dead_mask = self.life > self.max_life
        if np.any(dead_mask) and np.any(self.alive):
            dead_indices = np.nonzero(dead_mask)[0]
            self._respawn_particles(dead_indices)
            self.alive[dead_mask] = GL_FALSE

    def _init_particles(self):
        num_to_create = np.random.randint(0, self.max_per_frame)
        indices = np.arange(num_to_create)
        self._respawn_particles(indices)

    def _respawn_particles(self, indices):
        # init particles vectorized
        if len(indices) == 0:
            return
        idx = np.asarray(indices, dtype=int)
        count = idx.size
        EMIT_DIR = Vec3(0, 1, 0).to_numpy()
        SPREAD = 15.0
        rand_pos = np.random.rand(count, 1)
        # create direction vector
        rand_normals = np.random.normal(size=(count, 3))
        norms = np.linalg.norm(rand_normals, axis=1, keepdims=True)
        # ensure no division by zero
        norms[norms == 0] = 1
        rand_unit = rand_normals / norms
        directions = EMIT_DIR * rand_pos + rand_unit * SPREAD
        directions[:, 1] = np.abs(directions[:, 1])
        positions = np.tile(self._position.to_numpy().reshape(1, 3), (count, 1))
        colours = np.random.rand(count, 3)
        life = np.zeros(count, dtype=int)
        max_life = np.random.randint(self.life_range[0], self.life_range[1], size=count, dtype=int)
        # print(life, max_life)
        self.position[idx] = positions
        self.direction[idx] = directions
        self.colour[idx] = colours
        self.life[idx] = life
        self.max_life[idx] = max_life
