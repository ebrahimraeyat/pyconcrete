import pytest

import ezdxf

from pyconcrete.beamtype import beamtype, scalebeamtype, beamtypedxf

tars = []
y1 = -9.4
y2 = -3.4
tars.append([(-11.25, y1),
             (-11.25, y2),
             (121, y2)])
tars.append([(175, y2),
             (485.7, y2)])
tars.append([(641, y2),
             (843.75, y2),
             (843.75, y1)
             ])

prop1 = dict(spans_len=[204, 420, 350],
             beams_dimension=[(40, 45), (40, 45), (40, 45)],
             columns_width=dict(
    bot=[0, 45, 40, 50],
    top=[0, 45, 40, 45],),
    stirrups_len=[None, [85, 85], [85, 85]],
    axes_name=[('C', 1), ('D', 1), ('E', 1), ('F', 1)],)

prop2 = dict(spans_len=[204, 420, 350],
             beams_dimension=[(40, 60), (30, 60), (50, 60)],
             columns_width=dict(
    bot=[45, 45, 40, 50],
    top=[40, 45, 40, 45],),
    stirrups_len=[None, [115, 115], [85, 85]],
    axes_name=[('A', 1), ('B', 1), ('C', 1), ('D', 1)],)

prop3 = dict(spans_len=[204, 420, 350],
             beams_dimension=[(40, 40), (30, 40), (50, 40)],
             columns_width=dict(
    bot=[45, 45, 40, 50],
    top=[0, 0, 0, 0],),
    stirrups_len=[None, [115, 115], [85, 85]],
    axes_name=[('A', 1), ('B', 1), ('C', 1), ('D', 1)],)

prop4 = dict(spans_len=[204, 420, 350],
             beams_dimension=[(40, 40), (30, 40), (50, 40)],
             columns_width=dict(
    bot=[0, 0, 0, 0],
    top=[45, 45, 40, 50],),
    stirrups_len=[None, [115, 115], [85, 85]],
    axes_name=[('A', 1), ('B', 1), ('C', 1), ('D', 1)],)

prop5 = dict(spans_len=[295, 540],
             beams_dimension=[(40, 40), (40, 40)],
             columns_width=dict(
    bot=[45, 45, 40],
    top=[40, 45, 40],),
    stirrups_len=[None, [85, 85]],
    axes_name=[('A', 1), ('B', 1), ('C', 1)],
    top_add_rebars=tars,)


props = (prop1, prop2, prop3, prop4, prop5)

new_dwg = ezdxf.new('AC1024', setup=True)
msp = new_dwg.modelspace()
h = 1
v = 1
for i, prop in enumerate(props):
    sbt = scalebeamtype.ScaleBeamType(h, v, **prop)
    btdxf = beamtypedxf.BeamTypeDxf(sbt, new_dwg)
    btdxf.to_dxf()
    msp.add_blockref(sbt.uid, (200 / h, i * 130 / v))
new_dwg.saveas('/home/ebi/beamtype1.dxf')

# scaled beamtype
new_dwg = ezdxf.new('AC1024', setup=True)
msp = new_dwg.modelspace()
h = 100
v = 20
for i, prop in enumerate(props):
    sbt = scalebeamtype.ScaleBeamType(h, v, **prop)
    btdxf = beamtypedxf.BeamTypeDxf(sbt, new_dwg)
    btdxf.to_dxf()
    msp.add_blockref(sbt.uid, (200 / h, i * 130 / v))
new_dwg.saveas('/home/ebi/scaled_beamtype1.dxf')
