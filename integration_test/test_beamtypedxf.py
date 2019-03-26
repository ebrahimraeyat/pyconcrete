import pytest

import ezdxf

from pyconcrete.beamtype import beamtype, beamtypedxf


# @pytest.fixture
# def bt1():
bt1 = beamtype.BeamType(spans_len=[295, 540],
                        beams_dimension=[(40, 40), (40, 40)],
                        columns_width=dict(
    bot=[45, 45, 40],
    top=[40, 45, 40],),
    stirrups_len=[None, [85, 85]],
    axes_name=[('A', 1), ('B', 1), ('C', 1)],
)
# return bt1

bt2 = beamtype.BeamType(spans_len=[254, 620, 350],
                        beams_dimension=[(40, 40), (40, 45), (40, 50)],
                        columns_width=dict(
    bot=[45, 45, 40, 50],
    top=[40, 45, 40, 45],),
    stirrups_len=[None, [85, 85], [85, 85]],
    axes_name=[('A', 1), ('B', 1), ('C', 1), ('D', 1)],
)

bt3 = beamtype.BeamType(spans_len=[254, 620, 350],
                        beams_dimension=[(40, 40), (40, 30), (40, 40)],
                        columns_width=dict(
    bot=[45, 45, 40, 50],
    top=[40, 45, 40, 45],),
    stirrups_len=[None, [85, 85], [85, 85]],
    axes_name=[('A', 1), ('B', 1), ('C', 1), ('D', 1)],
)

new_dwg = ezdxf.new('AC1024', setup=True)
# dwg.layers.new(name='SAZE_DRAWINGS')
# btdxf1 = beamtypedxf.BeamTypeDxf(bt1, new_dwg)
# btdxf2 = beamtypedxf.BeamTypeDxf(bt2, new_dwg)
btdxf3 = beamtypedxf.BeamTypeDxf(bt3, new_dwg)
# btdxf1.to_dxf()
# btdxf2.to_dxf()
btdxf3.to_dxf()
msp = new_dwg.modelspace()
# msp.add_blockref(bt1.uid, (100, 150))
# msp.add_blockref(bt2.uid, (100, 0))
msp.add_blockref(bt3.uid, (100, 0))
new_dwg.saveas('/home/ebi/beamtype1.dxf')
