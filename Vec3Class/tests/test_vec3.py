from vec3 import Vec3


def test_default_vec3():
    v = Vec3()
    assert v.x == 0.0
    assert v.y == 0.0
    assert v.z == 0.0
