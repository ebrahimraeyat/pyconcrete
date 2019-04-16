import pytest
import numpy as np

from pyconcrete.beamtype import scalebeamtype as sbt
from pyconcrete.beamtype import beam as b

horizontal = 100
vertical = 20


@pytest.fixture
def sbt1():
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
    sbt1 = sbt.ScaleBeamType(horizontal=horizontal,
                             vertical=vertical,
                             spans_len=[295, 540],
                             beams_dimension=[(40, 40), (40, 40)],
                             columns_width=dict(
                                 bot=[45, 45, 40],
                                 top=[40, 45, 40],),
                             stirrups_len=[None, [85, 85]],
                             axes_name=[('A', 1), ('B', 1), ('C', 1)],
                             top_add_rebars=tars,
                             )
    return sbt1


@pytest.fixture
def b1():
    b1 = b.Beam(length=2.95,
                width=.40,
                height=2,
                columns_width=dict(
                    bot=dict(left=.45, right=.45,),
                    top=dict(left=.40, right=.45,),
                ),
                stirrup_len=None,
                first_stirrup_dist=5 / horizontal,
                col_extend_dist=13.75 / vertical,
                console_extend_dist=20 / horizontal,
                stirrup_dy=1.25 / vertical
                )
    return b1


@pytest.fixture
def b2():
    b2 = b.Beam(length=5.40,
                width=.40,
                height=2,
                columns_width=dict(
                    bot=dict(left=.45, right=.40,),
                    top=dict(left=.45, right=.40,),
                ),
                stirrup_len=[.85, .85],
                dx=2.95,
                first_stirrup_dist=5 / horizontal,
                col_extend_dist=13.75 / vertical,
                console_extend_dist=20 / horizontal,
                stirrup_dy=1.25 / vertical
                )
    return b2


def test_number_of_spans(sbt1):
    assert len(sbt1) == 2


def test_spans_len(sbt1):
    assert sbt1.spans_len == [2.95, 5.40]


def test_beams_dimension(sbt1):
    bd = [(.40, 2), (.40, 2)]
    assert sbt1.beams_dimension == bd


def test_columns_width(sbt1):
    cw = dict(
        bot=[.45, .45, .40],
        top=[.40, .45, .40],)
    assert sbt1.columns_width == cw


def test_stirrup_len(sbt1):
    assert sbt1.stirrups_len == [None, [.85, .85]]


def test_axes_name(sbt1):
    an = [('A', 1), ('B', 1), ('C', 1)]
    assert sbt1.axes_name == an


def test_beam_prop(sbt1, b1, b2):
    beam1, beam2 = sbt1.beams
    assert beam1 == b1
    assert beam2 == b2


def test_is_start_console(sbt1):
    assert sbt1.is_start_console == False


def test_is_end_console(sbt1):
    assert sbt1.is_end_console == False


def test_axes_polyline_points(sbt1):
    x1, x2, x3 = 0, 2.95, 2.95 + 5.40
    y1, y2 = -4.5, 2.5
    app = [
        [(x1, y1), (x1, y2)],
        [(x2, y1), (x2, y2)],
        [(x3, y1), (x3, y2)],
    ]
    assert sbt1.axes_polyline_points == app


def test_beams_dimensions_text(sbt1):
    bdt = ['40X40', '40X40']
    assert sbt1.beams_dimensions_text() == bdt


def test_max_beams_height(sbt1):
    assert sbt1.max_beams_height == 2


def test_center_of_beams_dist(sbt1):
    assert sbt1.center_of_beams_dist == [2.95 / 2, (2.95 + 5.40 / 2)]


def test_axes_dist(sbt1):
    axd = [0, 2.95, 8.35]
    assert pytest.approx(sbt1.axes_dist) == axd


def test_axes_dim_points(sbt1):
    x1, x2, x3 = 0, 2.95, 2.95 + 5.40
    y2 = sbt1.base_dim
    adp = [
        [(x1, y2), (x2, y2)],
        [(x2, y2), (x3, y2)],
    ]
    assert sbt1.axes_dim_points == adp


def test_top_polylines_points(sbt1, b1, b2):
    tpps = []
    tpps.append(b1.top_polyline_points)
    tpps.append(b2.top_polyline_points)
    np.testing.assert_allclose(sbt1.top_polylines_points, tpps)


def test_bot_polylines_points(sbt1, b1, b2):
    bpps = []
    bpps.append(b1.bot_polyline_points)
    bpps.append(b2.bot_polyline_points)
    np.testing.assert_allclose(sbt1.bot_polylines_points, bpps)


def test_stirrups_points(sbt1, b1, b2):
    sp = []
    sp.append(b1.stirrup_points)
    sp.append(b2.stirrup_points)
    assert sbt1.stirrups_points == sp


def test_edges_polyline_points(sbt1, b1, b2):
    epps = []
    epps.append(b1.left_edge_polyline)
    epps.append(b2.right_edge_polyline)
    assert sbt1.edges_polyline_points == epps


def test_top_main_rebar_points(sbt1):
    tmrp = ((-.165, -.4),
            (-.165, -.1),
            (8.49, -.1),
            (8.49, -.4))
    assert sbt1.top_main_rebar_points == tmrp


def test_bot_main_rebar_points(sbt1):
    bmrp = ((-.165, -1.6),
            (-.165, -1.9),
            (8.49, -1.9),
            (8.49, -1.6))
    np.testing.assert_allclose(sbt1.bot_main_rebar_points, bmrp)


def test_center_of_axis_circle_points(sbt1):
    coacps = ((0, 2.4), (2.95, 2.4), (8.35, 2.4))
    np.testing.assert_allclose(sbt1.center_of_axis_circle_points, coacps)


def test_axes_text(sbt1):
    at = ['A1', 'B1', 'C1']
    assert sbt1.axes_text == at


def test_scaled_beams_dimensions_text(sbt1):
    bdt = ['40X40', '40X40']
    assert sbt1.beams_dimensions_text() == bdt


def test_top_add_rebars(sbt1):
    tars = []
    y1 = -9.4 / 20
    y2 = -3.4 / 20
    tars.append([(-.1125, y1),
                 (-.1125, y2),
                 (1.21, y2)])
    tars.append([(1.75, y2),
                 (4.857, y2)])
    tars.append([(6.41, y2),
                 (8.4375, y2),
                 (8.4375, y1)
                 ])
    assert sbt1.top_add_rebars == tars


def test_bot_add_rebars(sbt1):
    assert sbt1.bot_add_rebars == []
