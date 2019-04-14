# from dataclasses import dataclass
from pyconcrete.point import Point
import copy

from pyconcrete.beamtype.beam import Beam


class ScaleBeam(Beam):
    def __init__(self,
                 horizontal=100,
                 vertical=20,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        self.horizontal = horizontal
        self.vertical = vertical
        self.scale()

    def scale(self):
        self._scale_constant()
        self._scale_columns_width()
        self._scale_stirrup_len()
        self.length /= self.horizontal
        self.width /= self.horizontal
        self.height /= self.vertical
        self.dx /= self.horizontal
        self.dy /= self.vertical

    def _scale_constant(self):
        self.first_stirrup_dist /= self.horizontal
        self.col_extend_dist /= self.vertical
        self.console_extend_dist /= self.horizontal
        self.stirrup_dy /= self.vertical

    def _scale_columns_width(self):
        w = self.columns_width_list
        self.columns_width['top']['left'] = w[0] / self.horizontal
        self.columns_width['top']['right'] = w[1] / self.horizontal
        self.columns_width['bot']['left'] = w[2] / self.horizontal
        self.columns_width['bot']['right'] = w[3] / self.horizontal

    def _scale_stirrup_len(self):
        if not self.stirrup_len:
            return
        for i, d in enumerate(self.stirrup_len):
            self.stirrup_len[i] = d / self.horizontal
