#ifndef VEC3_H_
#define VEC3_H_

struct Vec3
{
    Vec3()=default;
    Vec3(float _x, float _y, float _z) : m_x{_x},m_y{_y},m_z{_z}{}
    Vec3 operator *(float _f) const;
    Vec3 operator +(const Vec3 &_rhs) const;
    void operator +=(const Vec3 &_rhs);
    float m_x=0.0f;
    float m_y=0.0f;
    float m_z=0.0f;
};

#endif
