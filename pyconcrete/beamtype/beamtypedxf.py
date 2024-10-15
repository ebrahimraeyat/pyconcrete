import ezdxf

from pyconcrete.beamtype import beamtype as bt
from pyconcrete.point import Point



class BeamTypeDxf:
    def __init__(self,
                 beamtype: bt.BeamType,
                 dwg  # : ezdxf.drawing.Drawing
                 ):
        self.beamtype = beamtype
        self.dwg = dwg
        self.block = self.dwg.blocks.new(name=self.beamtype.uid)

    def add_top_polylines(self):
        for pt in self.beamtype.top_polylines_points:
            self.block.add_polyline2d(pt, dxfattribs={'color': 3})

    def add_bot_polylines(self):
        for pt in self.beamtype.bot_polylines_points:
            self.block.add_polyline2d(pt, dxfattribs={'color': 3})

    def add_edges_polyline(self):
        for pt in self.beamtype.edges_polyline_points:
            self.block.add_polyline2d(pt, dxfattribs={'color': 3})

    def add_axes_polyline(self):
        for pt in self.beamtype.axes_polyline_points:
            self.block.add_polyline2d(pt, dxfattribs={'color': 2, 'linetype': 'HIDDEN2'})

    def add_stirrups(self):
        for st in self.beamtype.stirrups_points:
            for pt in st:
                self.block.add_polyline2d(pt, dxfattribs={'color': 4})

    def add_axes_dim(self):
        pass

    def add_texts_dimension(self):
        texts = self.beamtype.beams_dimensions_text
        dist = self.beamtype.center_of_beams_dist
        for t, d in zip(texts, dist):
            p = (d, 0)
            self.block.add_text(
                t,
                dxfattribs={
                    'color': 2,
                    'style': 'SAZE_STYLE1',
                    'height': 4 / self.beamtype.vertical,  # constant
                }
            ).set_placement(p, None, align=ezdxf.enums.TextEntityAlignment.BOTTOM_CENTER)

    def add_dim_lines(self):
        d = self.beamtype.base_dim - 8 / self.beamtype.vertical
        for i, pt in enumerate(self.beamtype.axes_dim_points):
            self.block.add_aligned_dim(
                *pt,
                d,
                text=self.beamtype.spans_len_text[i],
                dimstyle='SAZE_DIM_STYLE',
                dxfattribs={'color': 2, })

    def add_axes_circle(self):
        for pt in self.beamtype.center_of_axis_circle_points:
            self.block.add_circle(center=pt, radius=10 / self.beamtype.vertical,
                                  dxfattribs={'color': 2})

    def add_axes_text(self):
        texts = self.beamtype.axes_text
        points = self.beamtype.center_of_axis_circle_points
        for t, pt in zip(texts, points):
            self.block.add_text(
                t,
                dxfattribs={'color': 3,
                            'height': 8 / self.beamtype.vertical,  # constant
                            'style': 'SAZE_STYLE1', }  # constant
            ).set_placement(pt, None, align=ezdxf.enums.TextEntityAlignment.MIDDLE_CENTER)

    def add_top_add_rebars(self):
        for pt in self.beamtype.top_add_rebars:
            self.block.add_polyline2d(pt, dxfattribs={'color': 6})
    
    def add_bot_add_rebars(self):
        for pt in self.beamtype.bot_add_rebars:
            self.block.add_polyline2d(pt, dxfattribs={'color': 6})
    
    def add_top_main_rebars(self):
        for pt in self.beamtype.top_main_rebars:
            self.block.add_polyline2d(pt, dxfattribs={'color': 6})

    def add_bot_main_rebars(self):
        for pt in self.beamtype.bot_main_rebars:
            self.block.add_polyline2d(pt, dxfattribs={'color': 6})

    def add_leaders(self):
        leaders_points = self.beamtype.leaders_points()
        rebars = self.beamtype._top_add_rebars + \
            self.beamtype._bot_add_rebars + \
            self.beamtype._top_main_rebars + \
            self.beamtype._bot_main_rebars
        for _rebar, pt in zip(rebars, leaders_points):
            self.block.add_leader(vertices=pt, dxfattribs={'color': 2})
            p1, p2 = self.leader_texts_pos(pt[1])
            self.block.add_text(_rebar.text, dxfattribs={'color': 3,
                                                         # 'style': 'OpenSans',
                                                         'height': 4 / self.beamtype.vertical,
                                                         }).set_placement(p1, None, align=ezdxf.enums.TextEntityAlignment.BOTTOM_RIGHT)
            self.block.add_text(_rebar.text_len, dxfattribs={'color': 2,
                                                             # 'style': 'OpenSans',
                                                             'height': 4 / self.beamtype.vertical,
                                                             }).set_placement(p2, None, align=ezdxf.enums.TextEntityAlignment.TOP_RIGHT)

            # msp.add_text('Text', dxfattribs={
            #     'style': 'OpenSans',
            #     'height': .25,
            # })..set_placement((2, 5), align=ezdxf.enums.TextEntityAlignment.BOTTOM_LEFT)

    def leader_texts_pos(self, p):
        p1 = Point(*p)
        x = 10 / self.beamtype.horizontal
        y = 2 / self.beamtype.vertical
        top_point = p1 - Point(x, 0)
        bot_point = p1 - Point(x, y)
        return tuple(top_point), tuple(bot_point)

    def add_stirrup_dim_lines(self):
        texts = self.beamtype.stirrups_text
        d = - 20 / self.beamtype.vertical
        for t, pt in zip(texts, self.beamtype.stirrup_dim_points):
            self.block.add_aligned_dim(
                *pt,
                d,
                text=t,
                dimstyle='STIRRUP_DIM_STYLE')

    def add_stirrup_len_text(self):
        texts = []
        for i in self.beamtype.stirrups_dist:
            texts += i
        d = -self.beamtype.max_beams_height - 7 / self.beamtype.vertical
        for t, pt in zip(texts, self.beamtype.stirrup_dim_points):
            self.block.add_aligned_dim(
                *pt,
                d,
                text=int(t),
                dimstyle='STIRRUP_LEN_STYLE')

    def to_dxf(self):
        self.add_top_polylines()
        self.add_bot_polylines()
        self.add_edges_polyline()
        self.add_axes_polyline()
        self.add_stirrups()
        self.add_texts_dimension()
        self.add_dim_lines()
        self.add_top_main_rebars()
        self.add_bot_main_rebars()
        self.add_axes_circle()
        self.add_axes_text()
        self.add_axes_dim()
        self.add_top_add_rebars()
        self.add_bot_add_rebars()
        self.add_leaders()
        self.add_stirrup_dim_lines()
        self.add_stirrup_len_text()
