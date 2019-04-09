import pytest

import ezdxf

from pyconcrete.beamtype import beamtype, beamtypedxf


bt1 = beamtype.BeamType(spans_len=[295, 540],
                        beams_dimension=[(40, 40), (40, 40)],
                        columns_width=dict(
    bot=[45, 45, 40],
    top=[40, 45, 40],),
    stirrups_len=[None, [85, 85]],
    axes_name=[('A', 1), ('B', 1), ('C', 1)],
)


bt2 = beamtype.BeamType(spans_len=[254, 420, 350],
                        beams_dimension=[(40, 45), (40, 45), (40, 45)],
                        columns_width=dict(
    bot=[45, 45, 40, 50],
    top=[40, 45, 40, 45],),
    stirrups_len=[None, [85, 85], [85, 85]],
    axes_name=[('C', 1), ('D', 1), ('E', 1), ('F', 1)],
)


bt3 = beamtype.BeamType(spans_len=[204, 420, 350],
                        beams_dimension=[(40, 40), (30, 40), (50, 40)],
                        columns_width=dict(
    bot=[45, 45, 40, 50],
    top=[40, 45, 40, 45],),
    stirrups_len=[None, [115, 115], [85, 85]],
    axes_name=[('A', 1), ('B', 1), ('C', 1), ('D', 1)],
)

new_dwg = ezdxf.new('AC1024', setup=True)
# dwg.layers.new(name='SAZE_DRAWINGS')
msp = new_dwg.modelspace()
for i, bt in enumerate((bt1, bt2, bt3)):
    btdxf = beamtypedxf.BeamTypeDxf(bt, new_dwg)
    btdxf.to_dxf()
    msp.add_blockref(bt.uid, (200, i * 150))
new_dwg.saveas('/home/ebi/beamtype1.dxf')
