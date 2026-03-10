import math


class Vec3:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, rhs):
        if not isinstance(rhs, Vec3):
            raise NotImplementedError
        return math.isclose(self.x, rhs.x) and math.isclose(self.y, rhs.y) and math.isclose(self.z, rhs.z)

    def __str__(self):
        return f"{self.x},{self.y},{self.z}"
