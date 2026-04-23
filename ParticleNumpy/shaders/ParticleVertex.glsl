#version 410 core

layout(location=0) in vec3 position;
layout(location=1) in vec3 colour;
uniform mat4 MVP;
out vec3 particle_colour;
void main()
{
    particle_colour = colour;
    gl_Position = MVP*vec4(position,1.0);
}
