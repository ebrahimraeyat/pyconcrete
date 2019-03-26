from dataclasses import dataclass


class Beam:
    id_ = 0
    first_stirrup_dist = 5
    col_extend_dist = 13.75

    def __init__(self,
                 length,
                 width,
                 height,
                 columns_width,
                 stirrup_len=None,
                 dx=0,
                 dy=0,
                 ):
        self.length = length
        self.width = width
        self.height = height
        self.columns_width = columns_width
        self.stirrup_len = stirrup_len
        self.dx = dx
        self.dy = dy
        Beam.increse_id()

    @property
    def coordinates(self):
        '''
        return top and bottom coordinate lines of beam
        p1, p2, p3, p4 as a dict of dict,
        x coordinate of ref. point = Axe of the left column,
        y coordinate of ref. point = top line of beam.
        if no column present, the line exted to the Axe of line,
        for example p2 in the below pic.

        Axe of left column
             |                                                  |
        |    |     |                                            |
        |    |     |                                            |
        |    |  p1 *-------------------------------------------*|p2  |
        |    |                                                  |    |
        |    |  p3 *---------------------------------------* p4 |    |
        |    |     |                                       |    |    |
        |    |     |                                       |    |    |
        '''
        dx1 = self.columns_width['top']['left']
        dx2 = self.columns_width['top']['right']
        dx3 = self.columns_width['bot']['left']
        dx4 = self.columns_width['bot']['right']
        p1 = (dx1 / 2 + self.dx, self.dy)
        p2 = (self.length - dx2 / 2 + self.dx, self.dy)
        p3 = (dx3 / 2 + self.dx, -self.height + self.dy)
        p4 = (self.length - dx4 / 2 + self.dx, -self.height + self.dy)
        coordinates = dict(
            top=dict(left=p1,
                     right=p2,),
            bot=dict(left=p3,
                     right=p4,),
        )
        return coordinates

    @property
    def stirrups_dist(self):
        dx1 = self.columns_width['bot']['left']
        dx2 = self.columns_width['bot']['right']
        if not self.stirrup_len:
            return [dx1 / 2 + Beam.first_stirrup_dist + self.dx,
                    self.length - dx2 / 2 - Beam.first_stirrup_dist + self.dx]
        else:
            x1 = dx1 / 2 + Beam.first_stirrup_dist + self.dx
            x2 = x1 + self.stirrup_len[0]
            x4 = self.length - dx2 / 2 - Beam.first_stirrup_dist + self.dx
            x3 = self.length - dx2 / 2 - self.stirrup_len[1] + self.dx
        return [x1, x2, x3, x4]

    @property
    def stirrup_points(self):
        y1 = -1.25
        y2 = -self.height + 1.25
        sp = []
        for x in self.stirrups_dist:
            sp.append([(x, y1), (x, y2)])
        return sp

    # def set_scale(self, horizontal=1, vertical=1):
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
    #     self.scale = dict(horizontal=horizontal, vertical=vertical)

    @property
    def columns_width_list(self):
        w1 = self.columns_width['top']['left']
        w2 = self.columns_width['top']['right']
        w3 = self.columns_width['bot']['left']
        w4 = self.columns_width['bot']['right']
        return [w1, w2, w3, w4]

    @classmethod
    def increse_id(cls):
        cls.id_ += 1

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
        points.append((x1, y1 + Beam.col_extend_dist))
        points.append(p1)
        points.append(p2)
        points.append((x2, y2 + Beam.col_extend_dist))
        return points

    @property
    def bot_polyline_points(self):
        points = []
        p1 = self.coordinates['bot']['left']
        p2 = self.coordinates['bot']['right']
        x1, y1 = p1
        x2, y2 = p2
        points.append((x1, y1 - Beam.col_extend_dist))
        points.append(p1)
        points.append(p2)
        points.append((x2, y2 - Beam.col_extend_dist))
        return points

    @property
    def left_edge_polyline(self):
        x, y1 = self.coordinates['bot']['left']
        _, y2 = self.coordinates['top']['left']
        dx = self.columns_width['bot']['left']
        p1 = (x - dx, y1 - Beam.col_extend_dist)
        p2 = (x - dx, y2 + Beam.col_extend_dist)
        return [p1, p2]

    @property
    def right_edge_polyline(self):
        x, y1 = self.coordinates['bot']['right']
        _, y2 = self.coordinates['top']['right']
        dx = self.columns_width['bot']['right']
        p1 = (x + dx, y1 - self.col_extend_dist)
        p2 = (x + dx, y2 + self.col_extend_dist)
        return [p1, p2]
