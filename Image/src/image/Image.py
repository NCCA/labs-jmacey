from dataclasses import dataclass

import numpy as np
from PIL import Image as PILImage
from PIL.Image import fromarray


@dataclass
class rgba:
    """A class to represent RGBA pixel data"""

    r: int = 0
    g: int = 0
    b: int = 0
    a: int = 255

    def __post_init__(self) -> None:
        """Validate RGBA values post init"""
        for component in ("r", "g", "b", "a"):
            value = getattr(self, component)
            if not isinstance(value, int) or not (0 <= value <= 255):
                raise ValueError(f"RGBA component {component} must be an int in the range 0-255 ")

    def as_tuple(self):
        return (self.r, self.g, self.b, self.a)


class ImageAccessError(Exception):
    pass


class Image:
    def __init__(self, width: int, height: int, fill_colour=None):
        """
        Image class generated with width, height and optional colour if none found it will be white. 
        """
        self._width = width
        self._height = height
        fill = self._validate_rgba(fill_colour)
        self._rgba_data = np.full((self._height, self._width, 4), fill, dtype=np.uint8)

    def _validate_rgba(self, fill_colour):
        match fill_colour:
            case None:
                return (255, 255, 255, 255)
            case rgba(r, g, b, a):
                return (r, g, b, a)
            case (r, g, b):
                return (r, g, b, 255)
            case (r, g, b, a):
                return (r, g, b, a)
            case _:
                raise TypeError(f"Invalid type for RGBA colour : {type(fill_colour).__name__}")

    def _check_bounds(self, x, y):
        if not (0 <= x < self._width and 0 <= y < self._height):
            raise IndexError(f"x,y values out of range {x=} {self.width=} {y=} {self.height=}")

    def get_pixel(self, x, y):
        self._check_bounds(x, y)
        return tuple(self._rgba_data[y, x])

    def set_pixel(self, x, y, value):
        self._check_bounds(x, y)
        v = self._validate_rgba(value)
        self._rgba_data[y, x] = v

    def save(self, name):
        img = PILImage.fromarray(self._rgba_data)
        img.save(name)

    def clear(self, colour):
        c = self._validate_rgba(colour)
        self._rgba_data[:] = c

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        raise ImageAccessError("Can't set read only property height")

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        raise ImageAccessError("Can't set read only property width")
