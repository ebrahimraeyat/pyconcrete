class Point:

    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if all((self.x == other.x,
                self.y == other.y,
                self.z == other.z)):
            return True
        return False

    def __repr__(self):
        return f'Point({self.x}, {self.y}, {self.z})'

    def plusx(self, dx):
        self.x += dx

    def to_tuple(self):
        return (self.x, self.y, self.z)

    def to_xytuple(self):
        return (self.x, self.y)
