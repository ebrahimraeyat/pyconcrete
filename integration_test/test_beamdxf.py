import ezdxf
from pyconcrete.beamtype import beam, beamdxf


b1 = beam.Beam(485, 40, 45, dict(bot=dict(left=50, right=40), top=dict(left=40, right=35)), [30, 460])

dwg = ezdxf.new('AC1024')
# dwg.layers.new(name='SAZE_DRAWINGS')
msp = dwg.modelspace()
name = 'beam1'
block = dwg.blocks.new(name=name)
b1_dxf = beamdxf.BeamDxf(b1, block)
b1_dxf.to_dxf()
msp.add_blockref(name, (0, 0))
dwg.saveas('/home/ebi/beam.dxf')
