# from dataclasses import dataclass, field
import uuid

from pyconcrete.beamtype import beam
from pyconcrete.point import Point
from pyconcrete.rebar import Rebar


class BeamType:

    def __init__(self, spans_len: list,
                 beams_dimension: list,
                 columns_width: dict,
                 stirrups_len: list,
                 axes_name: list,
                 stirrup_at: list=None,
                 stirrup_size: tuple=None,
                 extend_edge_len: int = 50,
                 base_dim: int = 42,  # 38,
                 extend_main_rebar: int = 6,
                 main_rebar_dx: int = 6,
                 main_rebar_dy: int = 2,
                 first_stirrup_dist=5,
                 col_extend_dist=13.75,
                 console_extend_dist=20,
                 stirrup_dy=1.25,
                 leader_dx=72,
                 leader_dy=30,
                 leader_offcet=5.5,
                 # top_main_rebars: dict = None,
                 # bot_main_rebars: dict = None,
                 top_add_rebars: list = [],
                 bot_add_rebars: list = [],
                 uid: str = None,
                 ):
        self.spans_len = spans_len
        self.beams_dimension = beams_dimension
        self.columns_width = columns_width
        self.stirrups_len = stirrups_len
        self.stirrup_at = stirrup_at
        self.stirrup_size = stirrup_size
        self.axes_name = axes_name
        self.extend_edge_len = extend_edge_len
        self.base_dim = base_dim
        self.extend_main_rebar = extend_main_rebar
        self.main_rebar_dx = main_rebar_dx
        self.main_rebar_dy = main_rebar_dy
        # self.add_rebar_dy = add_rebar_dy
        self.first_stirrup_dist = first_stirrup_dist
        self.col_extend_dist = col_extend_dist
        self.console_extend_dist = console_extend_dist
        self.stirrup_dy = stirrup_dy
        self.leader_dx = leader_dx
        self.leader_dy = leader_dy
        self.leader_offcet = leader_offcet
        self._top_add_rebars = top_add_rebars
        self._bot_add_rebars = bot_add_rebars
        self.uid = str(uuid.uuid4().int)
        self.spans_len_text = self._spans_len_text()
        self.beams_dimensions_text = self._beams_dimensions_text()
        self.stirrups_dist = self._stirrups_dist()
        self.stirrups_text = self._stirrups_text()

    def _spans_len_text(self):
        slt = []
        for len_ in self.spans_len:
            slt.append(str(len_))
        return slt

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
            b = beam.Beam(length=length,
                          width=width,
                          height=height,
                          columns_width=cw,
                          stirrup_len=stirrup_len,
                          stirrup_at=self.stirrup_at[i],
                          stirrup_size=self.stirrup_size[i],
                          dx=dx,
                          is_first=is_first,
                          is_last=is_last,
                          first_stirrup_dist=self.first_stirrup_dist,
                          col_extend_dist=self.col_extend_dist,
                          console_extend_dist=self.console_extend_dist,
                          stirrup_dy=self.stirrup_dy
                          )
            bs.append(b)
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
        y2 = self.base_dim
        # y2 = self.extend_edge_len
        app = []
        for i in range(self.__len__() + 1):
            x = self.axes_dist[i]
            app.append([
                (x, y1),
                (x, y2)
            ])
        return app

    def _beams_dimensions_text(self):
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
    def stirrup_dim_points(self):
        sdps = []
        for beam in self.beams:
            sdps += beam.stirrup_dim_points
        return sdps

    @property
    def edges_polyline_points(self):
        b1, b2 = self.beams[0], self.beams[-1]
        epps = []
        epps.append(b1.left_edge_polyline)
        epps.append(b2.right_edge_polyline)
        return epps

    def _left_right_polylines_x(self):
        p1, p2 = self.edges_polyline_points
        x1 = p1[0][0]
        x2 = p2[0][0]
        return x1, x2

    @property
    def top_main_rebar_points(self):
        x1, x2 = self._left_right_polylines_x()
        p1 = (x1 + self.main_rebar_dx, -self.main_rebar_dy - self.extend_main_rebar)
        p2 = (x1 + self.main_rebar_dx, -self.main_rebar_dy)
        p3 = (x2 - self.main_rebar_dx, -self.main_rebar_dy)
        p4 = (x2 - self.main_rebar_dx, -self.main_rebar_dy - self.extend_main_rebar)
        return p1, p2, p3, p4

    @property
    def bot_main_rebar_points(self):
        max_height = self.max_beams_height
        x1, x2 = self._left_right_polylines_x()
        y1 = -max_height + (self.main_rebar_dy + self.extend_main_rebar)
        y2 = -max_height + self.main_rebar_dy
        p1 = (x1 + self.main_rebar_dx, y1)
        p2 = (x1 + self.main_rebar_dx, y2)
        p3 = (x2 - self.main_rebar_dx, y2)
        p4 = (x2 - self.main_rebar_dx, y1)
        return p1, p2, p3, p4

    @property
    def center_of_axis_circle_points(self):
        pass

    @property
    def axes_text(self):
        return [f'{i[0]}{i[1]}' for i in self.axes_name]

    @property
    def top_add_rebars(self):
        tar_points = []
        for rebar in self._top_add_rebars:
            tar_points.append(rebar.points())
        return tar_points

    @top_add_rebars.setter
    def top_add_rebars(self):
        pass

    @property
    def bot_add_rebars(self):
        bar_points = []
        for rebar in self._bot_add_rebars:
            bar_points.append(rebar.points())
        return bar_points

    @bot_add_rebars.setter
    def bot_add_rebars(self):
        pass

    def rebar_target_point(self, rebar):
        xs = self.axes_dist
        x1, x2, y = rebar.x1, rebar.x2, rebar.y
        for x in xs:
            if x1 < x < x2:
                return Point(x - self.leader_offcet, y)
        return Point(*rebar.points_along()[0])

    def rebar_leader_points(self, rebar):
        if rebar.v_align == 'top':
            dy = self.leader_dy
        elif rebar.v_align == 'bot':
            dy = -self.leader_dy

        p1 = self.rebar_target_point(rebar)
        p2 = p1.plusy(dy)
        p3 = p2.plusx(-self.leader_dx)
        return tuple(p1), tuple(p2), tuple(p3)

    def leaders_points(self):
        lpts = []
        for rebar in self._top_add_rebars:
            lpts.append(self.rebar_leader_points(rebar))
        for rebar in self._bot_add_rebars:
            lpts.append(self.rebar_leader_points(rebar))
        return lpts

    def _stirrups_dist(self):
        ssd = []
        for beam in self.beams:
            ssd.append(beam.stirrups_len)
        return ssd

    def stirrup_count(self, stirrup_at, stirrups_len):
        sc = []
        l = len(stirrup_at)
        sc.append(int(stirrups_len[0] / stirrup_at[0]) + 1)

        if l == 3:
            sc.append(int(stirrups_len[1] / stirrup_at[1]))
            sc.append(int(stirrups_len[2] / stirrup_at[2]) + 1)
        return sc

    @property
    def stirrups_count(self):
        ssc = []
        for i, j in zip(self.stirrup_at, self.stirrups_dist):
            ssc.append(self.stirrup_count(i, j))
        return ssc

    def _stirrups_text(self):
        texts = []
        for a, b, c in zip(self.stirrups_count, self.stirrup_at, self.stirrup_size):
            for d, e in zip(a, b):
                texts.append(f'{d}~{c}@{e}')

        return texts
