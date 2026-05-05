#version 410 core
layout(location=0) out vec4 frag_colour;
in vec3 particle_colour;
void main()
{
    frag_colour.rgb=particle_colour;
}
