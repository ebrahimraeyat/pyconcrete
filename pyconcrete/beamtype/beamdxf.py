from pyconcrete.beamtype.beam import Beam
import ezdxf


class BeamDxf:

    def __init__(self, beam, block=None):
        '''
        msp: model space in ezdxf package
        '''
        self.beam = beam
        self.msp = block

    def to_dxf(self):
        self._top_bot_line_to_dxf()
        self._left_rigth_stirrups_to_dxf()
        self._dimensions_text_to_dxf()

    def _top_bot_line_to_dxf(self):
        p1 = self.coordinates['top']['left']
        p2 = self.coordinates['top']['right']
        p3 = self.coordinates['bot']['left']
        p4 = self.coordinates['bot']['right']
        self.msp.add_lwpolyline([p1, p2], dxfattribs={'color': 3})
        self.msp.add_lwpolyline([p3, p4], dxfattribs={'color': 3})

    def _left_rigth_stirrups_to_dxf(self):
        x1 = self.stirrups_x[0]
        x2 = self.stirrups_x[-1]
        y1 = self.coordinates['bot']['left'][1] + self.first_stirrup_dist
        y2 = self.coordinates['top']['left'][1] - self.first_stirrup_dist
        left_points = [(x1, y1), (x1, y2)]
        right_points = [(x2, y1), (x2, y2)]
        self.msp.add_lwpolyline(left_points, dxfattribs={'color': 4})
        self.msp.add_lwpolyline(right_points, dxfattribs={'color': 4})

    def _dimensions_text_to_dxf(self):
        align = 'BOTTOM_CENTER'
        x = (self.coordinates['top']['right'][0] - self.coordinates['top']['left'][0]) / 2
        y = 0
        p1 = (x, y)
        self.msp.add_text(f"{self.beam.width}X{self.beam.height}",
                          dxfattribs={'color': 2, 'height': 7}).set_placement(p1, align=align)

    @property
    def coordinates(self):
        return self.beam.coordinates

    @property
    def stirrups_x(self):
        return self.beam.stirrups_x

    @property
    def first_stirrup_dist(self):
        return self.beam.first_stirrup_dist

    @property
    def name(self):
        return f'beam{self.beam.id_}'
