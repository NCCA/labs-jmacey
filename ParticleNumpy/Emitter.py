import numpy as np


class Emitter:
    def __init__(self, num_particles):
        self.pos = np.random.uniform(-1, 1, size=(num_particles, 3)).astype(np.float32)
        self.colour = np.random.rand(num_particles, 3).astype(np.float32)
