import copy
from pyconcrete.beamtype.beamtype import BeamType
from pyconcrete.beamtype import beam


class ScaleBeamType(BeamType):
    def __init__(self,
                 horizontal=100,
                 vertical=20,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        self.horizontal = horizontal
        self.vertical = vertical
        self.scale()

    def _scale_spans_len(self):
        self.spans_len = [i / self.horizontal for i in self.spans_len]

    def _scale_beams_dimension(self):
        self.beams_dimension = [(i / self.horizontal, j / self.vertical)
                                for i, j in self.beams_dimension]

    def _scale_column_width(self):
        cw = {}
        for key in self.columns_width.keys():
            cw[key] = [i / self.horizontal
                       for i in self.columns_width[key]]
        self.columns_width = cw

    def _scale_stirrup_len(self):
        stirrups_len = []
        for i in self.stirrups_len:
            if i:
                tmp = []
                for j in i:
                    tmp.append(j / self.horizontal)
                stirrups_len.append(tmp)
            else:
                stirrups_len.append(i)
        self.stirrups_len = stirrups_len

    def _scale_top_add_rebars(self):
        scale_rebars = []
        rebars = copy.deepcopy(self._top_add_rebars)
        for rebar in rebars:
            rebar.scale(self.horizontal, self.vertical)
            scale_rebars.append(rebar)
        self._top_add_rebars = scale_rebars

    def _scale_constant(self):
        self.extend_edge_len /= self.vertical
        self.base_dim /= self.vertical
        self.extend_main_rebar /= self.vertical
        self.main_rebar_dx /= self.horizontal
        self.main_rebar_dy /= self.vertical
        self.first_stirrup_dist /= self.horizontal
        self.col_extend_dist /= self.vertical
        self.console_extend_dist /= self.horizontal
        self.stirrup_dy /= self.vertical

    def scale(self):
        self._scale_spans_len()
        self._scale_beams_dimension()
        self._scale_column_width()
        self._scale_stirrup_len()
        self._scale_constant()
        self._scale_top_add_rebars()

    @property
    def center_of_axis_circle_points(self):
        xs = self.axes_dist
        ys = len(xs) * [self.base_dim + 10 / self.vertical]  # constant 10: radius of circle
        return tuple(zip(xs, ys))
