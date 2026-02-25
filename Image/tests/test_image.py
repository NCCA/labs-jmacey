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


def test_image_red():
    img = Image(2, 3, (255, 0, 0, 255))
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = img.get_pixel(x, y)
            assert r == 255
            assert g == 0
            assert b == 0
            assert a == 255


def test_image_blue():
    img = Image(2, 3, (0, 0, 255, 255))
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = img.get_pixel(x, y)
            assert r == 0
            assert g == 0
            assert b == 255
            assert a == 255


def test_out_of_bounds():
    img = Image(2, 2)
    with pytest.raises(IndexError):
        _ = img.get_pixel(2, 2)


def test_set_pixel():
    img = Image(3, 1)
    img.set_pixel(0, 0, (255, 0, 0))
    img.set_pixel(1, 0, (0, 255, 0))
    img.set_pixel(2, 0, (0, 0, 255))
    assert img.get_pixel(0, 0) == (255, 0, 0, 255)
    assert img.get_pixel(1, 0) == (0, 255, 0, 255)
    assert img.get_pixel(2, 0) == (0, 0, 255, 255)
    img.save("rgb.png")
