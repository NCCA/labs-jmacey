from vec3 import Vec3


def test_default_vec3():
    v = Vec3()
    assert v.x == 0.0
    assert v.y == 0.0
    assert v.z == 0.0


def test_user_ctor():
    v = Vec3(0.5, -1.0, 20.0)
    assert v.x == 0.5
    assert v.y == -1.0
    assert v.z == 20.0
