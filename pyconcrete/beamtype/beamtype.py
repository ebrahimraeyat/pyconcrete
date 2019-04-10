# from dataclasses import dataclass, field
import uuid

from pyconcrete.beamtype import beam as b


class BeamType:

    def __init__(self, spans_len: list,
                 beams_dimension: list,
                 columns_width: dict,
                 stirrups_len: list,
                 axes_name: list,
                 extend_edge_len: int = 50,
                 base_dim: int = 38,
                 extend_main_rebar: int = 6,
                 top_main_rebars: dict = None,
                 bot_main_rebars: dict = None,
                 top_add_rebars: dict = None,
                 bot_add_rebars: dict = None,
                 uid: str = None,
                 ):
        self.spans_len = spans_len
        self.beams_dimension = beams_dimension
        self.columns_width = columns_width
        self.stirrups_len = stirrups_len
        self.axes_name = axes_name
        self.extend_edge_len = extend_edge_len
        self.base_dim = base_dim
        self.extend_main_rebar = extend_main_rebar
        self.uid = str(uuid.uuid4().int)

        # @dataclass
        # class BeamType:
        #     spans_len: list
        #     beams_dimension: list
        #     columns_width: dict
        #     stirrups_len: list
        #     axes_name: list
        #     extend_edge_len: int = 50
        #     base_dim: int = 38
        #     extend_main_rebar: int = 6
        #     top_main_rebars: dict = None
        #     bot_main_rebars: dict = None
        #     top_add_rebars: dict = None
        #     bot_add_rebars: dict = None
        #     uid: str = str(uuid.uuid4().int)

    def __len__(self):
        return len(self.spans_len)

    @property
    def beams(self):
        '''
        return beams of beamtype in a list, beams are
        Beam class.
        '''
        bs = []
        axes_dist = self.axes_dist
        for i in range(len(self)):
            length = self.spans_len[i]
            dimension = self.beams_dimension[i]
            width = dimension[0]
            height = dimension[1]
            top = self.columns_width['top'][i: i + 2]
            bot = self.columns_width['bot'][i: i + 2]
            cw = dict(
                bot=dict(left=bot[0], right=bot[1],),
                top=dict(left=top[0], right=top[1],),
            )
            stirrup_len = self.stirrups_len[i]
            dx = axes_dist[i]
            is_first = False
            is_last = False
            if i == 0:
                is_first = True
            if i == len(self) - 1:
                is_last = True
            beam = b.Beam(length=length,
                          width=width,
                          height=height,
                          columns_width=cw,
                          stirrup_len=stirrup_len,
                          dx=dx,
                          is_first=is_first,
                          is_last=is_last,
                          )
            bs.append(beam)
        return bs

    @property
    def is_start_console(self):
        return False

    @property
    def is_end_console(self):
        return False

    @property
    def axes_dist(self):
        '''
        return distance of axes in a list
        '''
        return [sum(self.spans_len[:i]) for i in range(self.__len__() + 1)]

    @property
    def axes_polyline_points(self):
        '''
        return points coordinate of axes line as
        a list of tuples
        '''
        y1 = -(self.max_beams_height + self.extend_edge_len)
        y2 = self.extend_edge_len
        app = []
        for i in range(self.__len__() + 1):
            x = self.axes_dist[i]
            app.append([
                (x, y1),
                (x, y2)
            ])
        return app

    def beams_dimensions_text(self):
        bdt = []
        for bd in self.beams_dimension:
            width, height = bd
            text = f'{width}X{height}'
            bdt.append(text)
        return bdt

    @property
    def max_beams_height(self):
        beams_height = [i[1] for i in self.beams_dimension]
        return max(beams_height)

    @property
    def center_of_beams_dist(self):
        x = self.axes_dist
        xcobd = []
        for i in range(self.__len__()):
            xcobd.append(
                x[i] +
                self.spans_len[i] / 2
            )
        return xcobd

    @property
    def axes_dim_points(self):
        '''
        return points coordinate for axes dimensions line
        '''
        x = self.axes_dist
        y = self.base_dim
        adp = []
        for i in range(self.__len__()):
            adp.append([
                (x[i], y),
                (x[i + 1], y)
            ])
        return adp

    @property
    def top_polylines_points(self):
        tpps = []
        for beam in self.beams:
            tpps.append(beam.top_polyline_points)
        return tpps

    @property
    def bot_polylines_points(self):
        bpps = []
        for beam in self.beams:
            bpps.append(beam.bot_polyline_points)
        return bpps

    @property
    def stirrups_points(self):
        sps = []
        for beam in self.beams:
            sps.append(beam.stirrup_points)
        return sps

    @property
    def edges_polyline_points(self):
        b1, b2 = self.beams[0], self.beams[-1]
        epps = []
        epps.append(b1.left_edge_polyline)
        epps.append(b2.right_edge_polyline)
        return epps

    def __left_right_polylines_x(self):
        p1, p2 = self.edges_polyline_points
        x1 = p1[0][0]
        x2 = p2[0][0]
        return x1, x2

    @property
    def top_main_rebar_points(self):
        self.main_rebar_dx = 6
        self.main_rebar_dy = 2
        x1, x2 = self.__left_right_polylines_x()
        p1 = (x1 + self.main_rebar_dx, -self.main_rebar_dy - self.extend_main_rebar)
        p2 = (x1 + self.main_rebar_dx, -self.main_rebar_dy)
        p3 = (x2 - self.main_rebar_dx, -self.main_rebar_dy)
        p4 = (x2 - self.main_rebar_dx, -self.main_rebar_dy - self.extend_main_rebar)
        return p1, p2, p3, p4

    @property
    def bot_main_rebar_points(self):
        self.main_rebar_dx = 6
        self.main_rebar_dy = 2
        max_height = self.max_beams_height
        x1, x2 = self.__left_right_polylines_x()
        y1 = -max_height + (self.main_rebar_dy + self.extend_main_rebar)
        y2 = -max_height + self.main_rebar_dy
        p1 = (x1 + self.main_rebar_dx, y1)
        p2 = (x1 + self.main_rebar_dx, y2)
        p3 = (x2 - self.main_rebar_dx, y2)
        p4 = (x2 - self.main_rebar_dx, y1)
        return p1, p2, p3, p4

    @property
    def center_of_axis_circle_points(self):
        xs = self.axes_dist
        ys = [self.base_dim + 10] * len(xs)  # constant 10: radius of circle
        return tuple(zip(xs, ys))

    @property
    def axes_text(self):
        return [f'{i[0]}{i[1]}' for i in self.axes_name]


# class Scaled_Beam_Type(BeamType):
#     def __init__(self, horizontal, vertical, **kwargs):
#         super().__init__(**kwargs)
#         self.horizontal = horizontal
#         self.vertical = vertical
