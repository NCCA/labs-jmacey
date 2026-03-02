from dataclasses import dataclass
from typing import Optional, Tuple, Union

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

    def as_tuple(self) -> Tuple[int, int, int, int]:
        """Return the RGBA values as a tuple."""
        return (self.r, self.g, self.b, self.a)


class ImageAccessError(Exception):
    """Exception raised for image access errors."""

    pass


class Image:
    def __init__(
        self,
        width: int,
        height: int,
        fill_colour: Optional[Union[rgba, Tuple[int, int, int], Tuple[int, int, int, int]]] = None,
    ) -> None:
        """
        Image class generated with width, height and optional colour.

        If fill_colour is None, it defaults to white (255, 255, 255, 255).

        Args:
            width (int): The width of the image.
            height (int): The height of the image.
            fill_colour (Optional[Union[rgba, Tuple[int, int, int], Tuple[int, int, int, int]]]):
                The colour to fill the image with. Defaults to None (white).
        """
        self._width = width
        self._height = height
        fill = self._validate_rgba(fill_colour)
        self._rgba_data = np.full((self._height, self._width, 4), fill, dtype=np.uint8)

    def _validate_rgba(
        self, fill_colour: Optional[Union[rgba, Tuple[int, int, int], Tuple[int, int, int, int]]]
    ) -> Tuple[int, int, int, int]:
        """
        Validate and convert the input colour to an RGBA tuple.

        Args:
            fill_colour (Union[rgba, Tuple[int, int, int], Tuple[int, int, int, int], None]): The colour to validate.

        Returns:
            Tuple[int, int, int, int]: The validated RGBA tuple.

        Raises:
            TypeError: If the input type is invalid.
        """
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

    def _check_bounds(self, x: int, y: int) -> None:
        """
        Check if the coordinates are within the image bounds.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.

        Raises:
            IndexError: If x or y are out of bounds.
        """
        if not (0 <= x < self._width and 0 <= y < self._height):
            raise IndexError(f"x,y values out of range {x=} {self.width=} {y=} {self.height=}")

    def get_pixel(self, x: int, y: int) -> Tuple[int, int, int, int]:
        """
        Get the pixel value at the specified coordinates.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.

        Returns:
            Tuple[int, int, int, int]: The RGBA value of the pixel.
        """
        self._check_bounds(x, y)
        return tuple(self._rgba_data[y, x])  # type: ignore

    def set_pixel(self, x: int, y: int, value: Union[rgba, Tuple[int, int, int], Tuple[int, int, int, int]]) -> None:
        """
        Set the pixel value at the specified coordinates.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
            value (Union[rgba, Tuple[int, int, int], Tuple[int, int, int, int]]): The new RGBA value.
        """
        self._check_bounds(x, y)
        v = self._validate_rgba(value)
        self._rgba_data[y, x] = v

    def save(self, name: str) -> None:
        """
        Save the image to a file.

        Args:
            name (str): The name of the file to save to.
        """
        img = PILImage.fromarray(self._rgba_data)
        img.save(name)

    def clear(self, colour: Optional[Union[rgba, Tuple[int, int, int], Tuple[int, int, int, int]]] = None) -> None:
        """
        Clear the image with the specified colour.

        Args:
            colour (Optional[Union[rgba, Tuple[int, int, int], Tuple[int, int, int, int]]]): The colour to clear with.
        """
        c = self._validate_rgba(colour)
        self._rgba_data[:] = c

    @property
    def height(self) -> int:
        """
        Get the height of the image.

        Returns:
            int: The height of the image.
        """
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        raise ImageAccessError("Can't set read only property height")

    @property
    def width(self) -> int:
        """
        Get the width of the image.

        Returns:
            int: The width of the image.
        """
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        raise ImageAccessError("Can't set read only property width")

    def line(
        self,
        sx: int,
        sy: int,
        ex: int,
        ey: int,
        colour: Optional[Union[rgba, Tuple[int, int, int], Tuple[int, int, int, int]]] = None,
    ) -> None:
        """
        Draw a line from (sx, sy) to (ex, ey) with the specified colour.

        Args:
            sx (int): The starting x-coordinate.
            sy (int): The starting y-coordinate.
            ex (int): The ending x-coordinate.
            ey (int): The ending y-coordinate.
            colour (Optional[Union[rgba, Tuple[int, int, int], Tuple[int, int, int, int]]]): The colour of the line.
        """
        dx, dy = abs(ex - sx), abs(ey - sy)
        x, y = sx, sy
        sx_sign = 1 if ex > sx else -1
        sy_sign = 1 if ey > sy else -1
        if dx > dy:
            err = dx / 2
            while x != ex:
                self.set_pixel(x, y, value=colour)
                err -= dy
                if err < 0:
                    y += sy_sign
                    err += dx
                x += sx_sign
        else:
            err = dy / 2
            while y != ey:
                self.set_pixel(x, y, value=colour)
                err -= dx
                if err < 0:
                    x += sx_sign
                    err += dy
                y += sy_sign
        self.set_pixel(ex, ey, value=colour)

    def rectangle(
        self,
        tx: int,
        ty: int,
        bx: int,
        by: int,
        colour: Optional[Union[rgba, Tuple[int, int, int], Tuple[int, int, int, int]]] = None,
    ) -> None:
        """
        Draw a filled rectangle defined by top-left (tx, ty) and bottom-right (bx, by).

        Args:
            tx (int): Top-left x-coordinate.
            ty (int): Top-left y-coordinate.
            bx (int): Bottom-right x-coordinate.
            by (int): Bottom-right y-coordinate.
            colour (Optional[Union[rgba, Tuple[int, int, int], Tuple[int, int, int, int]]]): The fill colour.
        """
        x0, x1 = sorted((tx, bx))
        y0, y1 = sorted((ty, by))
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                self.set_pixel(x, y, value=colour)


if __name__ == "__main__":
    # Create a red image using an rgba object
    red_colour = rgba(r=255, g=0, b=0)
    img_red = Image(512, 512, red_colour)
    img_red.save("red.png")

    # Create a green image using a tuple
    img_green = Image(512, 512, (0, 255, 0))
    img_green.save("green.png")

    # Create a blue image with transparency
    blue_colour = rgba(r=0, g=0, b=255, a=128)
    img_blue = Image(512, 512, blue_colour)
    img_blue.save("blue_transparent.png")

    # Create a default (white) image
    img_white = Image(256, 256)
    img_white.save("white.png")

    # Set a single pixel to black
    img_white.set_pixel(128, 128, rgba())  # rgba() defaults to black
    img_white.save("white_with_black_pixel.png")

    # Clear the image to a semi-transparent purple
    purple_colour = rgba(r=128, g=0, b=128, a=128)
    img_white.clear(purple_colour)
    img_white.save("purple.png")

    # Draw some lines on a new image
    img_lines = Image(512, 512, (255, 255, 255))
    img_lines.line(0, 0, 511, 511, (255, 0, 0))  # Red diagonal
    img_lines.line(0, 511, 511, 0, (0, 0, 255))  # Blue diagonal
    img_lines.save("lines.png")

    # Draw some rectangles on a new image
    img_rects = Image(512, 512, (255, 255, 255))
    img_rects.rectangle(50, 50, 200, 200, (0, 255, 0))  # Green square
    img_rects.rectangle(300, 100, 450, 400, rgba(128, 0, 128))  # Purple rectangle
    img_rects.save("rectangles.png")

    print("Generated test images.")
