from .point import Point


class Rebar:
    '''
    base class for rebars
    '''

    def __init__(self,
                 length: int=1,
                 diameter: int=20,
                 count: int=1,
                 insert: tuple=(0, 0),
                 v_align: str='top',    # top, bot
                 extend_main_rebar: int = 6,
                 ):
        self.length = length
        self.diameter = diameter
        self.count = count
        self.insert = insert
        self.v_align = v_align
        self.extend_main_rebar = extend_main_rebar
        self.text_len = self._text_len()

    @property
    def x1(self):
        return self.base_points()[0][0]

    @property
    def x2(self):
        return self.base_points()[1][0]

    @property
    def y(self):
        return self.insert[1]

    def scale(self, h, v):
        self.length /= h
        self.extend_main_rebar /= v
        p = Point.scale(*self.insert, h, v)
        self.insert = tuple(p)

    def points(self):
        '''
        return points of rebar in a list.
        list contain pairs of (x, y) coordinates
        '''
        p2 = Point(*self.insert).plusx(self.length)
        return [self.insert, tuple(p2)]

    def base_points(self):
        '''
        using base point for calculating points_along in
        inheritance class
        '''
        p2 = Point(*self.insert).plusx(self.length)
        return [self.insert, tuple(p2)]

    def points_along(self):
        _p1, _p2 = self.base_points()
        p1 = Point(*_p1)
        p2 = Point(*_p2)
        p_midle = (p1 + p2) / 2
        p_left = (p1 + p_midle) / 2
        p_rigth = (p_midle + p2) / 2
        return [tuple(p_left), tuple(p_midle), tuple(p_rigth)]

    @property
    def text(self):
        '''
        return text in format 'count~diameter'
        '''
        return f'{self.count}~{self.diameter}'

    def _text_len(self):
        return f'L={self.real_length:.0f}'

    @property
    def real_length(self):
        return self.length

    def __repr__(self):
        return f'{self.text}, L={self.real_length}'


class LRebar(Rebar):
    '''
    add bending to one side of straight rebar and return
    points of rebar in pair of (x, y),  3 points
    '''

    def __init__(self,
                 h_align: str='left',    # left, right
                 *args,
                 **kwargs,
                 ):
        super().__init__(*args, **kwargs)
        # self.v_align = v_align
        self.h_align = h_align

    def points(self):
        pts = super().points()

        if self.h_align == 'left':
            join_point = pts[0]
        elif self.h_align == 'right':
            join_point = pts[1]

        if self.v_align == 'top':
            add_pt = tuple(Point(*join_point).plusy(-self.extend_main_rebar))
        if self.v_align == 'bot':
            add_pt = tuple(Point(*join_point).plusy(self.extend_main_rebar))

        if self.h_align == 'left':
            pts.insert(0, add_pt)
        elif self.h_align == 'right':
            pts.append(add_pt)
        return pts


class URebar(Rebar):
    '''
    add bending to both side of straight rebar and return
    points of rebar in pair of (x, y), 4 points
    '''

    def __init__(self,
                 *args,
                 **kwargs
                 ):
        super().__init__(*args, **kwargs)

    def points(self):
        p2, p3 = super().points()
        if self.v_align == 'top':
            sign = -1
        elif self.v_align == 'bot':
            sign = 1

        p1 = tuple(Point(*p2).plusy(sign * self.extend_main_rebar))
        p4 = tuple(Point(*p3).plusy(sign * self.extend_main_rebar))

        return [p1, p2, p3, p4]
