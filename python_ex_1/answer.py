import abc
import math


class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    # Using @property decorator for getter/setter
    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, val):
        if val <= 0:
            raise ValueError("Radius of circle must be greater than 0")
        self._r = val

    # Shape parent class methods implementation
    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r
