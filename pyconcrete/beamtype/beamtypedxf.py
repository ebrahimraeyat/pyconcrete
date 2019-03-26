import ezdxf

from pyconcrete.beamtype import beamtype as bt


class BeamTypeDxf:
    def __init__(self,
                 beamtype: bt.BeamType,
                 dwg: ezdxf.drawing.Drawing
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
            self.block.add_polyline2d(pt, dxfattribs={'color': 2})

    def add_stirrups(self):
        for st in self.beamtype.stirrups_points:
            for pt in st:
                self.block.add_polyline2d(pt, dxfattribs={'color': 4})

    def add_axes_dim(self):
        pass

    def add_texts_dimension(self):
        texts = self.beamtype.beams_dimensions_text()
        dist = self.beamtype.center_of_beams_dist
        for t, d in zip(texts, dist):
            p = (d, 0)
            self.block.add_text(
                t, dxfattribs={'color': 2, 'height': 10}  # constant
            ).set_pos(p, align='BOTTOM_CENTER')

    def add_dim_lines(self):
        for pt in self.beamtype.axes_dim_points:
            self.block.add_aligned_dim(
                pt[0],
                pt[1],
                self.beamtype.base_dim,
                dxfattribs={'color': 2, })

    def to_dxf(self):
        self.add_top_polylines()
        self.add_bot_polylines()
        self.add_edges_polyline()
        self.add_axes_polyline()
        self.add_stirrups()
        self.add_texts_dimension()
        self.add_dim_lines()
        # self.add_axes_dim()
