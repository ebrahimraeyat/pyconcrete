from dataclasses import dataclass
import numpy as np


@dataclass
class Point:
    x: float
    y: float

    def plusx(self, dx):
        return Point(self.x + dx, self.y)

    def plusy(self, dy):
        return Point(self.x, self.y + dy)

    def scale(self, h=1, v=1):
        self.x *= h
        self.y *= v

    @classmethod
    def scale(cls, x, y, h, v):
        return cls(x / h, y / v)

    def __eq__(self, other):
        return all((
            np.allclose(self.x, other.x),
            np.allclose(self.y, other.y),
        ))

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Point(
            self.x - other.x,
            self.y - other.y
        )

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __iter__(self):
        '''
        for implementing tuple type of point
        '''
        yield self.x
        yield self.y

    def __truediv__(self, a):
        return Point(self.x / a, self.y / a)
