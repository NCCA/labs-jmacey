#!/usr/bin/env -S uv run --script

import OpenGL.GL as gl
from ncca.ngl import FirstPersonCamera, ShaderLib, VAOFactory, VAOType, Vec3, VertexData
from PySide6.QtGui import QSurfaceFormat
from PySide6.QtOpenGL import QOpenGLWindow
from PySide6.QtWidgets import QApplication

from Emitter import Emitter


class MainWindow(QOpenGLWindow):
    def __init__(self):
        super().__init__()

    def initializeGL(self):
        print("initializeGL")
        self.camera = FirstPersonCamera(Vec3(0, 0, 10), Vec3(0, 0, 0), Vec3(0, 1, 0), 45.0)
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glEnable(gl.GL_MULTISAMPLE)
        ShaderLib.load_shader("ParticleShader", "shaders/ParticleVertex.glsl", "shaders/ParticleFragment.glsl")
        ShaderLib.use("ParticleShader")
        gl.glClearColor(0.4, 0.4, 0.4, 1.0)
        self.emitter = Emitter(100000)
        self.vao = VAOFactory.create_vao(VAOType.MULTI_BUFFER, gl.GL_POINTS)
        with self.vao as vao:
            data = VertexData(data=[], size=0)
            vao.set_data(data, index=0)
            vao.set_data(data, index=1)

    def paintGL(self):
        gl.glPointSize(1)
        gl.glViewport(0, 0, self.width, self.height)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        ShaderLib.use("ParticleShader")
        ShaderLib.set_uniform("MVP", self.camera.get_vp())
        with self.vao as vao:
            data = VertexData(data=self.emitter.pos.flatten(), size=self.emitter.pos.nbytes)
            vao.set_data(data, index=0)
            vao.set_vertex_attribute_pointer(0, 3, gl.GL_FLOAT, 0, 0)
            data = VertexData(data=self.emitter.colour.flatten(), size=self.emitter.colour.nbytes)
            vao.set_data(data, index=1)
            vao.set_vertex_attribute_pointer(1, 3, gl.GL_FLOAT, 0, 0)
            vao.set_num_indices(len(self.emitter.pos))
            vao.draw()

    def resizeGL(self, w, h):
        self.width = w
        self.height = h
        ratio = self.devicePixelRatio()
        self.camera.set_projection(45.0, (w * ratio / h * ratio), 0.05, 200)


def main():
    app = QApplication()
    format = QSurfaceFormat()
    format.setMajorVersion(4)
    format.setMinorVersion(6)
    format.setProfile(QSurfaceFormat.CoreProfile)
    QSurfaceFormat.setDefaultFormat(format)
    win = MainWindow()
    win.resize(1024, 720)
    win.show()
    app.exec()


if __name__ == "__main__":
    main()
