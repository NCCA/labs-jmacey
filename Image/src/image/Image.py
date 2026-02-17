from dataclasses import dataclass


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
    def __init__(self, width, height):
        self._width = width
        self._height = height

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
