import ezdxf

from pyconcrete.beamtype import beamtype, scalebeamtype, beamtypedxf
from pyconcrete import rebar

# y2 = -3.4
# left_rebar = rebar.LRebar(length=132.2, insert=(-11.25, y2))
# mid_rebar = rebar.Rebar(length=310.7, insert=(175, y2))
# right_rebar = rebar.LRebar(length=202.75,
#                            h_align='right',
#                            insert=(641, y2))
# tars = [left_rebar, mid_rebar, right_rebar]

# y1 = -40 + 3.4
# bot_left_rebar = rebar.LRebar(length=122, insert=(-11.25, y1), h_align='left', v_align='bot')
# bot_mid_rebar = rebar.Rebar(length=295, insert=(200, y1))
# bot_right_rebar = rebar.LRebar(length=202.75,
#                                h_align='right',
#                                v_align='bot',
#                                insert=(641, y1))
# bars = [bot_left_rebar, bot_mid_rebar, bot_right_rebar]
axe_y = 'A'
prop1 = dict(spans_len=[92, 465, 650, 260, 107],
             beams_dimension=[(30, 55)] * 5,
             columns_width=dict(
    bot=[0, 45, 45, 45, 45, 0],
    top=[0, 45, 45, 45, 45, 0],),
    stirrups_len=[None, [85, 85], [120, 120], None, None],
    axes_name=[(axe_y, ''), (axe_y, 1), (axe_y, 2), (axe_y, 3), (axe_y, 4), (axe_y, '')],)

axe_y = 'B'
prop2 = dict(spans_len=[92, 465, 650, 260],
             beams_dimension=[(30, 40)] * 4,
             columns_width=dict(
    bot=[0, 0, 45, 45, 0],
    top=[0, 0, 45, 45, 0],),
    stirrups_len=[None, [85, 85], [120, 120], None],
    axes_name=[(axe_y, ''), (axe_y, 1), (axe_y, 2), (axe_y, 3), (axe_y, 4)],)

axe_y = 'C'
prop3 = dict(spans_len=[92, 465, 650, 260],
             beams_dimension=[(30, 40)] * 4,
             columns_width=dict(
    bot=[0, 45, 45, 45, 45],
    top=[0, 45, 45, 45, 45],),
    stirrups_len=[None, [85, 85], [120, 120], None],
    axes_name=[(axe_y, ''), (axe_y, 1), (axe_y, 2), (axe_y, 3), (axe_y, 4)],)

# prop2 = dict(spans_len=[204, 420, 350],
#              beams_dimension=[(40, 60), (30, 60), (50, 60)],
#              columns_width=dict(
#     bot=[45, 45, 40, 50],
#     top=[40, 45, 40, 45],),
#     stirrups_len=[None, [115, 115], [85, 85]],
#     axes_name=[('A', 1), ('B', 1), ('C', 1), ('D', 1)],)

# prop3 = dict(spans_len=[204, 420, 350],
#              beams_dimension=[(40, 40), (30, 40), (50, 40)],
#              columns_width=dict(
#     bot=[45, 45, 40, 50],
#     top=[0, 0, 0, 0],),
#     stirrups_len=[None, [115, 115], [85, 85]],
#     axes_name=[('A', 1), ('B', 1), ('C', 1), ('D', 1)],)

# prop4 = dict(spans_len=[204, 420, 350],
#              beams_dimension=[(40, 40), (30, 40), (50, 40)],
#              columns_width=dict(
#     bot=[0, 0, 0, 0],
#     top=[45, 45, 40, 50],),
#     stirrups_len=[None, [115, 115], [85, 85]],
#     axes_name=[('A', 1), ('B', 1), ('C', 1), ('D', 1)],)

# prop5 = dict(spans_len=[295, 540],
#              beams_dimension=[(40, 40), (40, 40)],
#              columns_width=dict(
#     bot=[45, 45, 40],
#     top=[40, 45, 40],),
#     stirrups_len=[None, [85, 85]],
#     axes_name=[('A', 1), ('B', 1), ('C', 1)],
#     top_add_rebars=tars,
#     bot_add_rebars=bars)


props = (prop1, prop2, prop3)  # , prop4, prop5)

# scaled beamtype h=100, v=25
new_dwg = ezdxf.readfile('/home/ebi/TEMPLATE.dxf')
msp = new_dwg.modelspace()
h = 100
v = 25
for i, prop in enumerate(props):
    sbt = scalebeamtype.ScaleBeamType(h, v, **prop)
    btdxf = beamtypedxf.BeamTypeDxf(sbt, new_dwg)
    btdxf.to_dxf()
    msp.add_blockref(sbt.uid, (200 / h, i * 130 / v))
new_dwg.saveas('/home/ebi/beamtype100.dxf')

# scaled beamtype h = 75, v = 20
new_dwg = ezdxf.readfile('/home/ebi/TEMPLATE.dxf')
msp = new_dwg.modelspace()
h = 75
v = 25
for i, prop in enumerate(props):
    sbt = scalebeamtype.ScaleBeamType(h, v, **prop)
    btdxf = beamtypedxf.BeamTypeDxf(sbt, new_dwg)
    btdxf.to_dxf()
    msp.add_blockref(sbt.uid, (200 / h, i * 130 / v))
new_dwg.saveas('/home/ebi/beamtype75.dxf')
