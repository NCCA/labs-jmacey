import math
import random

from Vec3 import Vec3


class Random:
    """
    Utility class for generating random floats and vectors.
    """

    @staticmethod
    def random_float(mult: float = 1.0) -> float:
        """
        Returns a random float in the range [-1, 1], scaled by `mult`.

        Args:
            mult (float): Multiplier for the random value.

        Returns:
            float: Random float in [-mult, mult].
        """
        return random.uniform(-1.0, 1.0) * mult

    @staticmethod
    def random_positive_float(mult: float = 1.0) -> float:
        """
        Returns a random float in the range [0, 1], scaled by `mult`.

        Args:
            mult (float): Multiplier for the random value.

        Returns:
            float: Random float in [0, mult].
        """
        return random.uniform(0.0, 1.0) * mult

    @staticmethod
    def random_vec3(mult: float = 1.0) -> Vec3:
        """
        Returns a Vec3 with each component in the range [-1, 1], scaled by `mult`.

        Args:
            mult (float): Multiplier for each component.

        Returns:
            Vec3: Random vector with components in [-mult, mult].
        """
        return Vec3(Random.random_float(mult), Random.random_float(mult), Random.random_float(mult))

    @staticmethod
    def random_positive_vec3(mult: float = 1.0) -> Vec3:
        """
        Returns a Vec3 with each component in the range [0, 1], scaled by `mult`.

        Args:
            mult (float): Multiplier for each component.

        Returns:
            Vec3: Random vector with components in [0, mult].
        """
        return Vec3(
            Random.random_positive_float(mult), Random.random_positive_float(mult), Random.random_positive_float(mult)
        )

    @staticmethod
    def random_vector_on_sphere(radius: float = 1.0) -> Vec3:
        """
        Returns a random Vec3 located on the surface of a sphere with the given radius.

        Args:
            radius (float): Radius of the sphere.

        Returns:
            Vec3: Random vector on the sphere's surface.
        """
        phi = Random.random_positive_float(math.pi * 2.0)
        costheta = Random.random_float()
        u = Random.random_positive_float()
        theta = math.acos(costheta)
        r = radius * (u ** (1.0 / 3.0))
        return Vec3(r * math.sin(theta) * math.cos(phi), r * math.sin(theta) * math.sin(phi), r * math.cos(theta))
