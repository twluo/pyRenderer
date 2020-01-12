import numpy as np
import numbers
import math


class Vec3:
    def __init__(self, x=0, y=None, z=None):
        if y is None and z is None:
            self.x = x
            self.y = x
            self.z = x
        else:
            self.x = x
            self.y = 0 if y is None else y
            self.z = 0 if z is None else z

    def __str__(self):
        return str(self.to_array())

    def __add__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, numbers.Real):
            return Vec3(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, numbers.Real):
            return Vec3(self.x - other, self.y - other, self.z - other)

    def __mul__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, numbers.Real):
            return Vec3(self.x * other, self.y * other, self.z * other)

    def __floordiv__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)
        elif isinstance(other, numbers.Real):
            return Vec3(self.x / other, self.y / other, self.z / other)

    def __truediv__(self, other):
        if isinstance(other, Vec3):
            return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)
        elif isinstance(other, numbers.Real):
            return Vec3(self.x / other, self.y / other, self.z / other)

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __iadd__(self, other):
        self = self + other
        return self

    def __isub__(self, other):
        self = self - other
        return self

    def __imul__(self, other):
        self = self * other
        return self

    def __ifloordiv__(self, other):
        self = self // other
        return self

    def __itruediv__(self, other):
        self = self / other
        return self

    def __eq__(self, other):
        return self.x is other.x and self.y is other.y and self.z is other.z

    def to_array(self):
        return [self.x, self.y, self.z]

    def dot(self, other):
        if isinstance(other, Vec3):
            return np.dot(self.to_array(), other.to_array())

    def cross(self, other):
        if isinstance(other, Vec3):
            return np.cross(self.to_array(), other.to_array())

    def length2(self):
        return self.dot(self)

    def length(self):
        return math.sqrt(self.length2())

    def normalized(self):
        return self // self.length()

    def normalize(self):
        unit = self.normalized()
        self.x = unit.x
        self.y = unit.y
        self.z = unit.z
        return self


a = Vec3(3, 0, 0)
b = Vec3(3, 0, 0)
print(a != b)
print(a.dot(a))
print(a.normalize())
print(a)
