# import ezdxf
# from pyconcrete.beamtype import beam, beamdxf


# b1 = beam.Beam(485, 40, 45, dict(bot=dict(left=50, right=40), top=dict(left=40, right=35)), [30, 460])

# b2 = beam.Beam(length=485,
#                width=40,
#                height=45,
#                columns_width=dict(
#                    bot=dict(left=50, right=40,),
#                    top=dict(left=0, right=0,)),
#                stirrup_len=None,
#                is_first=True,
#                is_last=True,
#                )

# dwg = ezdxf.new('AC1024')
# # dwg.layers.new(name='SAZE_DRAWINGS')
# msp = dwg.modelspace()
# beams = [b1, b2]
# for i, b in enumerate(beams):
#     name = b.id_
#     block = dwg.blocks.new(name=name)
#     b_dxf = beamdxf.BeamDxf(b, block)
#     b_dxf.to_dxf()
#     msp.add_blockref(name, (0, i * 150))

# dwg.saveas('/home/ebi/beam.dxf')
