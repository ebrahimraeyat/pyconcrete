import pytest

import ezdxf

from pyconcrete.beamtype import beamtypedxf as btdxf
from pyconcrete.beamtype import beamtype as bt
from .test_beamtype import bt1


@pytest.fixture
def btdxf1(bt1):
    dwg = ezdxf.new('ac1024')
    btdxf1 = btdxf.BeamTypeDxf(bt1, dwg)
    return btdxf1


def test_beamtype_type(bt1):
    assert isinstance(bt1, bt.BeamType)


def test_dwg_type(btdxf1):
    assert isinstance(btdxf1.dwg, ezdxf.drawing.Drawing)


def test_add_top_polylines(btdxf1):
    pass


def test_add_bot_polylines(btdxf1):
    pass


def test_add_edges_polyline(btdxf1):
    pass


def test_add_axes_polyline(btdxf1):
    pass


def test_add_stirrups(btdxf1):
    pass


def test_add_axes_dim(btdxf1):
    pass


def test_add_texts_dimension(btdxf1):
    pass


def test_add_dim_lines(btdxf1):
    pass


def test_add_top_main_rebar(btdxf1):
    pass


def test_add_bot_main_rebar(btdxf1):
    pass


def test_add_axes_circle(btdxf1):
    pass


def test_add_axes_text(btdxf1):
    pass
