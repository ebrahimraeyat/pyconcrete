# pyconcrete
python module for drawing concrete plan details.

it aims to draw such a beam and columns at the end.

![image](https://user-images.githubusercontent.com/8196112/55085621-97acb100-50c4-11e9-91e6-7afcf2d7dbbc.png)

![image](https://user-images.githubusercontent.com/8196112/55085845-f70ac100-50c4-11e9-98c4-05240751b4d5.png)


It includes BeamType class that itself includes number of Beams class.
at present it can draw beamtype shape, beamsize text, dimension lines and axes lines.

## Dependencies
- python >= 3.7
- ezdxf

## Usage

This example show how you can create BeamType and then export that to dxf file
with ezdxf python package for example.

```python
import ezdxf

from pyconcrete.beamtype import beamtype, scalebeamtype, beamtypedxf
from pyconcrete import rebar

y2 = -3.4
left_rebar = rebar.LRebar(length=132.2, insert=(-11.25, y2))
mid_rebar = rebar.Rebar(length=310.7, insert=(175, y2))
right_rebar = rebar.LRebar(length=202.75,
                           h_align='right',
                           insert=(641, y2))
tars = [left_rebar, mid_rebar, right_rebar]

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

# scaled beamtype h=75, v=20
new_dwg = ezdxf.readfile('/home/ebi/TEMPLATE.dxf')
msp = new_dwg.modelspace()
h = 75
v = 20
for i, prop in enumerate(props):
    sbt = scalebeamtype.ScaleBeamType(h, v, **prop)
    btdxf = beamtypedxf.BeamTypeDxf(sbt, new_dwg)
    btdxf.to_dxf()
    msp.add_blockref(sbt.uid, (200 / h, i * 130 / v))
new_dwg.saveas('/home/ebi/beamtype75.dxf')
```


## output

This is output at peresent, but I'll add styles to seems look better!


![image](https://user-images.githubusercontent.com/8196112/57562900-82f25700-73ac-11e9-8137-ed819e3b7a66.png)





