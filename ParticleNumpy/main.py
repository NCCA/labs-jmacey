#!/usr/bin/env -S uv run --script

import OpenGL.GL as gl
from ncca.ngl import (
    DefaultShader,
    FirstPersonCamera,
    Primitives,
    Prims,
    ShaderLib,
    VAOFactory,
    VAOType,
    Vec3,
    VertexData,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QSurfaceFormat
from PySide6.QtOpenGL import QOpenGLWindow
from PySide6.QtWidgets import QApplication

from Emitter import Emitter


class MainWindow(QOpenGLWindow):
    def __init__(self):
        super().__init__()
        self.animate = False
        self.keys_pressed = set()
        self.rotate = False
        self.original_x_pos = 0
        self.original_y_pos = 0

    def initializeGL(self):
        print("initializeGL")
        self.camera = FirstPersonCamera(Vec3(0, 5, 10), Vec3(0, 0, 0), Vec3(0, 1, 0), 45.0)
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glEnable(gl.GL_MULTISAMPLE)
        ShaderLib.load_shader("ParticleShader", "shaders/ParticleVertex.glsl", "shaders/ParticleFragment.glsl")
        ShaderLib.use("ParticleShader")
        gl.glClearColor(0.4, 0.4, 0.4, 1.0)
        self.emitter = Emitter(Vec3(0, 0, 0), 10000)
        self.vao = VAOFactory.create_vao(VAOType.MULTI_BUFFER, gl.GL_POINTS)
        with self.vao as vao:
            data = VertexData(data=[], size=0)
            vao.set_data(data, index=0)
            vao.set_data(data, index=1)

        Primitives.create(Prims.TRIANGLE_PLANE, "ground", 50, 50, 20, 20, Vec3(0, 1, 0))

        self.startTimer(30)

    def paintGL(self):
        gl.glPointSize(4)
        gl.glViewport(0, 0, self.width, self.height)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        ShaderLib.use("ParticleShader")
        ShaderLib.set_uniform("MVP", self.camera.get_vp())
        self._process_camera_movement()
        with self.vao as vao:
            data = VertexData(data=self.emitter.position.flatten(), size=self.emitter.position.nbytes)
            vao.set_data(data, index=0)
            vao.set_vertex_attribute_pointer(0, 3, gl.GL_FLOAT, 0, 0)
            data = VertexData(data=self.emitter.colour.flatten(), size=self.emitter.colour.nbytes)
            vao.set_data(data, index=1)
            vao.set_vertex_attribute_pointer(1, 3, gl.GL_FLOAT, 0, 0)
            vao.set_num_indices(len(self.emitter.position))
            vao.draw()
            ShaderLib.use(DefaultShader.COLOUR)
            ShaderLib.set_uniform("Colour", 0.0, 0.8, 0.0, 1.0)
            ShaderLib.set_uniform("MVP", self.camera.get_vp())
            Primitives.draw("ground")

    def _process_camera_movement(self):
        x_dir = 0.0
        y_dir = 0.0
        for key in self.keys_pressed:
            if key == Qt.Key_Left:
                y_dir = -1.0
            elif key == Qt.Key_Right:
                y_dir = 1.0
            elif key == Qt.Key_Up:
                x_dir = 1.0
            elif key == Qt.Key_Down:
                x_dir = -1.0
        if x_dir != 0.0 or y_dir != 0.0:
            self.camera.move(x_dir, y_dir, 0.1)

    def keyPressEvent(self, event):
        key = event.key()
        self.keys_pressed.add(key)
        if key == Qt.Key_Escape:
            self.close()
        elif key == Qt.Key_S:
            self.emitter.update(0.01)
            self.update()
        elif key == Qt.Key_Space:
            self.animate ^= True
        self.update()

    def keyReleaseEvent(self, event):
        key = event.key()
        self.keys_pressed.discard(key)
        self.update()

    def mousePressEvent(self, event):
        position = event.position()
        if event.button() == Qt.LeftButton:
            self.original_x_pos = position.x()
            self.original_y_pos = position.y()
            self.rotate = True

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.rotate = False

    def mouseMoveEvent(self, event):
        if self.rotate and event.buttons() == Qt.LeftButton:
            position = event.position()
            diff_x = position.x() - self.original_x_pos
            diff_y = position.y() - self.original_y_pos
            self.original_x_pos = position.x()
            self.original_y_pos = position.y()
            self.camera.process_mouse_movement(diff_x, -diff_y)
            self.update()

    def resizeGL(self, w, h):
        self.width = w
        self.height = h
        ratio = self.devicePixelRatio()
        self.camera.set_projection(45.0, (w * ratio / h * ratio), 0.05, 200)

    def timerEvent(self, event):
        if self.animate:
            self.emitter.update(0.01)
            self.update()


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
