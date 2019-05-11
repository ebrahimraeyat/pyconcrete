from unittest.mock import Mock, patch
import pytest
from pyconcrete.beamtype import beamdxf as bdxf
import ezdxf


@pytest.fixture
def beam1():
    p1 = (20, 0)
    p2 = (467.5, 0)
    p3 = (25, -45)
    p4 = (465, -45)
    __coordinates = dict(
        top=dict(left=p1, right=p2,),
        bot=dict(left=p3, right=p4,)
    )
    __stirrups_dist = [30, 115, 380, 460]
    __columns_width = dict(
        bot=dict(left=50, right=40,),
        top=dict(left=40, right=35,),
    )
    return dict(coordinates=__coordinates,
                stirrups_dist=__stirrups_dist,
                columns_width=__columns_width,
                first_stirrup_dist=5,
                width=40,
                height=45,
                # scale=dict(horizontal=1, vertical=1),
                )


def test_type_of_beam_dxf():
    beam = Mock()
    dwg = ezdxf.new('AC1032')
    block = dwg.blocks.new(name='beam1')
    msp_beam = bdxf.BeamDxf(beam, block)
    assert isinstance(msp_beam.msp, ezdxf.layouts.blocklayout.BlockLayout)


def test_top_bot_line_coordinates(beam1):
    beam = Mock()
    beam.coordinates = dict()
    dwg = ezdxf.new('AC1032')
    block = dwg.blocks.new(name='beam1')
    with patch.dict(beam.coordinates, beam1['coordinates']):
        msp_beam = bdxf.BeamDxf(beam, block)
        msp_beam._top_bot_line_to_dxf()
        top_points = [(20, 0, 0, 0, 0), (467.5, 0, 0, 0, 0)]
        bot_points = [(25, -45, 0, 0, 0), (465, -45, 0, 0, 0)]
        top_line = msp_beam.msp.query('LWPOLYLINE')[0]
        bot_line = msp_beam.msp.query('LWPOLYLINE')[1]
        with top_line.points() as pts:
            assert top_points == pts
        with bot_line.points() as pts:
            assert bot_points == pts


def test_left_right_stirrup(beam1):
    beam = Mock()
    dwg = ezdxf.new('AC1032')
    block = dwg.blocks.new(name='beam1')
    with patch.dict(beam.__dict__, beam1):
        msp_beam = bdxf.BeamDxf(beam, block)
        msp_beam._left_rigth_stirrups_to_dxf()
        left_points = [(30, -40, 0, 0, 0), (30, -5, 0, 0, 0)]
        right_points = [(460, -40, 0, 0, 0), (460, -5, 0, 0, 0)]
        left_line = msp_beam.msp.query('LWPOLYLINE')[0]
        right_line = msp_beam.msp.query('LWPOLYLINE')[1]
        with left_line.points() as pts:
            assert left_points == pts
        with right_line.points() as pts:
            assert right_points == pts


def test_beam_text_dimensions(beam1):
    beam = Mock()
    dwg = ezdxf.new('AC1032')
    block = dwg.blocks.new(name='beam1')
    with patch.dict(beam.__dict__, beam1):
        msp_beam = bdxf.BeamDxf(beam, block)
        msp_beam._dimensions_text_to_dxf()
        text = msp_beam.msp.query('TEXT')[0]
        align, pos = text.get_pos()[0:2]
        assert align == 'BOTTOM_CENTER'
        assert pos == (223.75, 0)
