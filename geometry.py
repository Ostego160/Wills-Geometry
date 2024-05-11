import numpy as np
import math
import vector
import tkinter as tk #just for the Typing

class Geometry:
    CIRCLE_RADIUS = 2

    def __init__(self, w: int, h: int, d: int) -> None:
        """
        Constructor of the Geometry
        :param w:
            Width of the cube
        :param h:
            Height of the cube
        :param d:
            Depth of the cube
        """
        self.w, self.h, self.d = int(w), int(h), int(d)
        self.size = self.w * self.h * self.d

        self.points = [None] * self.size
        self.scalar = 1

    def get_index(self, x: int, y: int, z:int) -> int:
        """
        Method to convert 3D coordinates to 1D index of an array
        :param x,y,z:
            Coordinate to convert
        :return:
            Returns the integer index of the 3D coordinate
        """
        return (z*self.h + y)*self.w + x
    def get_point(self, x: int, y: int, z:int) -> np.array:
        """
        Method to retrieve a point/vector from the geometry
        :param x,y,z:
            Coordinate of the vector
        :return:
            Returns the vector at the coordinate
        """
        return self.points[self.get_index(x,y,z)]

    def set_point(self, x: int, y: int, z:int, vec: np.array) -> None:
        """
        Method to set a point/vector in the geometry
        :param x,y,z:
            Coordinate of the vector
        :return:
            Returns the vector at the coordinate
        """
        self.points[self.get_index(x,y,z)] = vec

    def reformat_and_set_scalar(self, num: float) -> None:
        """
        Method to reset the geometry and apply a scalar
        :param num:
            Scalar to apply to the cube
        :return:
        """
        self.scalar = num
        self.points = [None] * self.size
        cx, cy, cz = int((self.w * self.scalar) / 2), int((self.h * self.scalar) / 2), int((self.d * self.scalar) / 2)

        count  = 0

        for z in range(self.d):
            for y in range(self.h):
                for x in range(self.w):
                    self.points[count] = vector.new(num * x - cx, num * y - cy, num * z - cz)
                    count += 1

    def apply_function(self, index: int) -> None:
        """
        Method to apply a multivariate function to the geometry
        :param index:
            Index of the function to use
        :return:
        """
        for z in range(self.d):
            for y in range(self.h):
                for x in range(self.w):
                    vec = self.get_point(x, y, z)
                    vector.apply_function(vec, index)

    def rotate(self, theta: float, phi: float) -> None:
        """
        Method to rotate the Geometry
        :param theta:
            Theta angle to rotate
        :param phi:
            Phi angle to rotate
        :return:
        """
        for z in range(self.d):
            for y in range(self.h):
                for x in range(self.w):
                    vec = self.get_point(x, y, z)
                    vector.rotate(vec, theta, phi)

    def z_sort(self) -> None:
        """
        Method to z sort points in the geometry
        :return:
        """
        self.points = sorted(self.points, key=lambda vec: vec[2], reverse=False)

    def draw_to_canvas(self, canvas: tk.Canvas, offset_x: float, offset_y: float) -> None:
        """
        :param canvas:
            TKinter canvas to draw to
        :param offset_x:
            X Offset for centering
        :param offset_y:
            Y Offset for centering
        :return:
        """
        i = Geometry.CIRCLE_RADIUS

        for vec in self.points:
            vx, vy, vz = vector.get(vec)
            canvas.create_oval(vx - i + offset_x, vy - i + offset_y, vx + i + offset_x, vy + i + offset_y, fill = 'blue', outline='red', stipple='gray50')
