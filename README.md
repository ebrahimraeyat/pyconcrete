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
left_rebar = rebar.LRebar(count=2, length=132.2, insert=(-11.25, y2))
mid_rebar = rebar.Rebar(count=3, diameter=16, length=310.7, insert=(175, y2))
right_rebar = rebar.LRebar(length=202.75,
                           h_align='right',
                           insert=(641, y2))
tars = [left_rebar, mid_rebar, right_rebar]

y1 = -40 + 3.4
bot_left_rebar = rebar.LRebar(length=122, insert=(-11.25, y1), h_align='left', v_align='bot')
bot_mid_rebar = rebar.Rebar(length=295, insert=(200, y1), v_align='bot')
bot_right_rebar = rebar.LRebar(length=202.75,
                               h_align='right',
                               v_align='bot',
                               insert=(641, y1))
bars = [bot_left_rebar, bot_mid_rebar, bot_right_rebar] 


prop5 = dict(spans_len=[295, 540],
             beams_dimension=[(40, 40), (40, 40)],
             columns_width=dict(
    bot=[45, 45, 40],
    top=[40, 45, 40],),
    stirrups_len=[None, [85, 85]],
    stirrup_at=[(8.5,), (8.5, 17, 8.5)],
    stirrup_size=(8, 10),
    axes_name=[('A', 1), ('B', 1), ('C', 1)],
    top_add_rebars=tars,
    bot_add_rebars=bars)

props = (prop5,)

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


![image](https://user-images.githubusercontent.com/8196112/57662418-add6e800-7604-11e9-811f-ea7d3e66746a.png)






