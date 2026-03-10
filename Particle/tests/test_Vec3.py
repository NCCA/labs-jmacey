import pytest

from Vec3 import Vec3


def test_default_vec3():
    v = Vec3()
    assert v.x == pytest.approx(0.0)
    assert v.y == pytest.approx(0.0)
    assert v.z == pytest.approx(0.0)


def test_eq():
    v = Vec3()
    assert v == Vec3()


def test_param_construct():
    v = Vec3(0.1, 2.2, 3.0)
    assert v.x == pytest.approx(0.1)
    assert v.y == pytest.approx(2.2)
    assert v.z == pytest.approx(3.0)
