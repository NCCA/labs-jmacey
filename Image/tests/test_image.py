import pytest

from image import Image, ImageAccessError, rgba


def test_rgba_default():
    p = rgba()
    assert p.r == 0
    assert p.g == 0
    assert p.b == 0
    assert p.a == 255


def test_rgba_user():
    p = rgba(1, 2, 3, 4)
    assert p.r == 1
    assert p.g == 2
    assert p.b == 3
    assert p.a == 4


@pytest.mark.parametrize("arg,value", [("r", -1), ("g", 256), ("b", 1000), ("a", -1000), ("b", "one")])
def test_invalid_values(arg, value):
    with pytest.raises(ValueError):
        kwargs = {arg: value}
        rgba(**kwargs)


@pytest.fixture
def red() -> rgba:
    return rgba(255, 0, 0)


def test_as_tuple(red):
    assert red.as_tuple() == (255, 0, 0, 255)


def test_default_image_ctor():
    img = Image(20, 30)
    assert img.width == 20
    assert img.height == 30


@pytest.fixture
def small_image() -> Image:
    return Image(10, 12)


def test_change_size(small_image):
    with pytest.raises(ImageAccessError):
        small_image.width = 100
    with pytest.raises(ImageAccessError):
        small_image.height = 100
