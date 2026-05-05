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


def test_mul_vec3():
    a = Vec3(1, 2, 3)
    b = Vec3(2, 2, 2)
    result = a * b
    assert result.x == pytest.approx(2)
    assert result.y == pytest.approx(4)
    assert result.z == pytest.approx(6)
    result = a * 3
    assert result.x == pytest.approx(3)
    assert result.y == pytest.approx(6)
    assert result.z == pytest.approx(9)
    with pytest.raises(TypeError):
        _ = a * str()


def test_add():
    a = Vec3(1, 2, 3)
    b = Vec3(2, 2, 2)
    result = a + b
    assert result.x == pytest.approx(3)
    assert result.y == pytest.approx(4)
    assert result.z == pytest.approx(5)
    with pytest.raises(TypeError):
        _ = a + str()
