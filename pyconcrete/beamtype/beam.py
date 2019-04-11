from dataclasses import dataclass
from pyconcrete.point import Point


class Beam:
    id_ = 0
    first_stirrup_dist = 5
    col_extend_dist = 13.75
    console_extend_dist = 20
    stirrup_dy = 1.25

    def __init__(self,
                 length,
                 width,
                 height,
                 columns_width,
                 stirrup_len=None,
                 dx=0,
                 dy=0,
                 is_first=False,
                 is_last=False,
                 scale=(1, 1),
                 ):
        self.length = length
        self.width = width
        self.height = height
        self.columns_width = columns_width
        self.stirrup_len = stirrup_len
        self.dx = dx
        self.dy = dy
        self.is_first = is_first
        self.is_last = is_last
        self.scale = scale
        self.scale_constant()
        self.id_ = id(self)

    def scale_constant(self):
        h, v = self.scale
        self.first_stirrup_dist /= h
        self.col_extend_dist /= v
        self.console_extend_dist /= h
        self.stirrup_dy /= v

    @property
    def coordinates(self):
        '''
        return top and bottom coordinate lines of beam
        p1, p2, p3, p4 as a dict of dict,
        x coordinate of ref. point = Axe of the left column,
        y coordinate of ref. point = top line of beam.
        if no column present, the line exted to the Axe of line,
        for example p2 in the below pic. if beam is_first or is_last is True and no
        column present, top or bottom line continue for FIRST_LAST_LINE_CONTINUE
        value from the axis (p3 in pic, is_first=True)

        Axe of left column
             |                                                  |
        |    |     |                                            |
        |    |     |                                            |
        |    |  p1 *-------------------------------------------*|p2  |
        |    |                                                  |    |
      p3*--------------------------------------------------* p4 |    |
             |                                             |    |    |
             |                                             |    |    |
        '''
        dx1 = self.columns_width['top']['left']
        dx2 = self.columns_width['top']['right']
        dx3 = self.columns_width['bot']['left']
        dx4 = self.columns_width['bot']['right']
        move_point = Point(self.dx, self.dy)
        p1 = Point(dx1 / 2, 0) + move_point
        p2 = Point(self.length - dx2 / 2, 0) + move_point
        p3 = Point(dx3 / 2, -self.height) + move_point
        p4 = Point(self.length - dx4 / 2, -self.height) + move_point
        extend = self.console_extend_dist
        if self.is_first:
            if dx1 == 0 and dx3 == 0:
                p1 = p1.plusx(-extend)
                p3 = p3.plusx(-extend)
            if dx1 == 0 and dx3 != 0:
                p1 = p1.plusx(-dx3 / 2)  # constant value, -20
            if dx3 == 0 and dx1 != 0:
                p3 = p3.plusx(-dx1 / 2)
        if self.is_last:
            if dx2 == 0 and dx4 == 0:
                p2 = p2.plusx(extend)
                p4 = p4.plusx(extend)
            elif dx2 == 0 and dx4 != 0:
                p2 = p2.plusx(dx4 / 2)
            if dx4 == 0 and dx2 != 0:
                p4 = p4.plusx(dx2 / 2)
        coordinates = dict(
            top=dict(left=tuple(p1),
                     right=tuple(p2),),
            bot=dict(left=tuple(p3),
                     right=tuple(p4),),
        )
        return coordinates

    @property
    def stirrups_dist(self):
        dx1 = self.columns_width['bot']['left']
        if dx1 == 0:
            dx1 = self.columns_width['top']['left']
        dx2 = self.columns_width['bot']['right']
        if dx2 == 0:
            dx2 = self.columns_width['top']['right']
        if not self.stirrup_len:
            return [dx1 / 2 + self.first_stirrup_dist + self.dx,
                    self.length - dx2 / 2 - self.first_stirrup_dist + self.dx]
        else:
            x1 = dx1 / 2 + self.first_stirrup_dist + self.dx
            x2 = x1 + self.stirrup_len[0]
            x4 = self.length - dx2 / 2 - self.first_stirrup_dist + self.dx
            x3 = self.length - dx2 / 2 - self.stirrup_len[1] + self.dx
        return [x1, x2, x3, x4]

    @property
    def stirrup_points(self):
        y1 = -self.stirrup_dy
        y2 = -self.height + self.stirrup_dy
        sp = []
        for x in self.stirrups_dist:
            sp.append([(x, y1), (x, y2)])
        return sp

    # @property
    # def scale(self):
    #     return self._scale

    # @scale.setter
    # def scale(self, value):
    #     horizontal, vertical = value
    #     self.first_stirrup_dist /= horizontal
    #     self.col_extend_dist /= vertical
    #     self.length /= horizontal
    #     self.width /= horizontal
    #     self.height /= vertical
    #     w = self.columns_width_list
    #     self.columns_width['top']['left'] = w[0] / horizontal
    #     self.columns_width['top']['right'] = w[1] / horizontal
    #     self.columns_width['bot']['left'] = w[2] / horizontal
    #     self.columns_width['bot']['right'] = w[3] / horizontal
    #     for i, d in enumerate(self.stirrup_len):
    #         self.stirrup_len[i] = d / horizontal
    #     self._scale = dict(horizontal=horizontal, vertical=vertical)

    @property
    def columns_width_list(self):
        w1 = self.columns_width['top']['left']
        w2 = self.columns_width['top']['right']
        w3 = self.columns_width['bot']['left']
        w4 = self.columns_width['bot']['right']
        return [w1, w2, w3, w4]

    # # @classmethod
    # def id_(self):
    #     self.id_ =

    def __eq__(self, other):
        if all([
            self.length == other.length,
            self.width == other.width,
            self.height == other.height,
            self.columns_width == other.columns_width,
            self.stirrup_len == other.stirrup_len
        ]):
            return True
        return False

    def __repr__(self):
        return f"\nlength = {self.length}, \
                 \nwidth = {self.width}, \
                 \nheight = {self.height}, \
                 \ncolumns_width = {self.columns_width}, \
                 \nstirrup_len = {self.stirrup_len}"

    @property
    def top_polyline_points(self):
        '''
        return a list of points for top polyline of beam
        in pair of (x, y) in a list
        pn*                                                 *pm
          |                                                 |
          |                                                 |
          |                                                 |
        p1*_________________________________________________*p2

        '''
        points = []
        p1 = self.coordinates['top']['left']
        p2 = self.coordinates['top']['right']
        x1, y1 = p1
        x2, y2 = p2
        if self.columns_width['top']['left']:
            points.append((x1, y1 + self.col_extend_dist))
        points.append(p1)
        points.append(p2)
        if self.columns_width['top']['right']:
            points.append((x2, y2 + self.col_extend_dist))
        return points

    @property
    def bot_polyline_points(self):
        points = []
        p1 = self.coordinates['bot']['left']
        p2 = self.coordinates['bot']['right']
        x1, y1 = p1
        x2, y2 = p2
        if self.columns_width['bot']['left']:
            points.append((x1, y1 - self.col_extend_dist))
        points.append(p1)
        points.append(p2)
        if self.columns_width['bot']['right']:
            points.append((x2, y2 - self.col_extend_dist))
        return points

    @property
    def left_edge_polyline(self):
        x, y1 = self.coordinates['bot']['left']
        _, y2 = self.coordinates['top']['left']
        dx = self.columns_width['bot']['left']
        p1 = Point(x - dx, y1)
        p2 = Point(x - dx, y2)
        if self.columns_width['bot']['left']:
            p1 = p1.plusy(-self.col_extend_dist)
        if self.columns_width['top']['left']:
            p2 = p2.plusy(self.col_extend_dist)
        return [tuple(p1), tuple(p2)]

    @property
    def right_edge_polyline(self):
        x, y1 = self.coordinates['bot']['right']
        _, y2 = self.coordinates['top']['right']
        dx = self.columns_width['bot']['right']
        p1 = Point(x + dx, y1)
        p2 = Point(x + dx, y2)
        if self.columns_width['bot']['right']:
            p1 = p1.plusy(-self.col_extend_dist)
        if self.columns_width['top']['right']:
            p2 = p2.plusy(self.col_extend_dist)
        return [tuple(p1), tuple(p2)]
