import pytest
import numpy as np

from pyconcrete.beamtype import beamtype as bt
from pyconcrete.beamtype import beam as b
from pyconcrete import rebar
from pyconcrete.point import Point


@pytest.fixture
def bt1():
    y2 = -3.4
    left_rebar = rebar.LRebar(length=132.2, insert=(-11.25, y2))
    mid_rebar = rebar.Rebar(length=310.7, insert=(175, y2))
    right_rebar = rebar.LRebar(length=202.75,
                               h_align='right',
                               insert=(641, y2))
    tars = [left_rebar, mid_rebar, right_rebar]

    bt1 = bt.BeamType(spans_len=[295, 540],
                      beams_dimension=[(40, 40), (40, 40)],
                      columns_width=dict(bot=[45, 45, 40],
                                         top=[40, 45, 40],),
                      stirrups_len=[None, [85, 85]],
                      stirrup_at=[(8.5,), (8.5, 17, 8.5)],
                      stirrup_size=(8, 8),
                      axes_name=[('A', 1), ('B', 1), ('C', 1)],
                      top_add_rebars=tars,
                      )
    return bt1


@pytest.fixture
def b1():
    b1 = b.Beam(length=295,
                width=40,
                height=40,
                columns_width=dict(bot=dict(left=45, right=45,),
                                   top=dict(left=40, right=45,),),
                stirrup_len=None,
                )
    return b1


@pytest.fixture
def b2():
    b2 = b.Beam(length=540,
                width=40,
                height=40,
                columns_width=dict(bot=dict(left=45, right=40,),
                                   top=dict(left=45, right=40,),),
                stirrup_len=[85, 85],
                dx=295,
                )
    return b2


def test_number_of_spans(bt1):
    assert len(bt1) == 2


def test_spans_len(bt1):
    assert bt1.spans_len == [295, 540]


def test_beams_dimension(bt1):
    bd = [(40, 40), (40, 40)]
    assert bt1.beams_dimension == bd


def test_columns_width(bt1):
    cw = dict(
        bot=[45, 45, 40],
        top=[40, 45, 40],)
    assert bt1.columns_width == cw


def test_stirrup_len(bt1):
    assert bt1.stirrups_len == [None, [85, 85]]


def test_axes_name(bt1):
    an = [('A', 1), ('B', 1), ('C', 1)]
    assert bt1.axes_name == an


def test_type_of_beams(b1, b2):
    assert isinstance(b1, b.Beam)
    assert isinstance(b2, b.Beam)


def test_beam_prop(bt1, b1, b2):
    beam1, beam2 = bt1.beams
    assert beam1 == b1
    assert beam2 == b2


def test_is_start_console(bt1):
    assert bt1.is_start_console == False


def test_is_end_console(bt1):
    assert bt1.is_end_console == False


def test_axes_polyline_points(bt1):
    x1, x2, x3 = 0, 295, 295 + 540
    y1, y2 = -90, 50
    app = [
        [(x1, y1), (x1, y2)],
        [(x2, y1), (x2, y2)],
        [(x3, y1), (x3, y2)],
    ]
    assert bt1.axes_polyline_points == app


def test_beams_dimensions_text(bt1):
    assert hasattr(bt1, 'beams_dimensions_text')
#     bdt = ['40X40', '40X40']
#     assert bt1.beams_dimensions_text() == bdt


def test_max_beams_height(bt1):
    assert bt1.max_beams_height == 40


def test_center_of_beams_dist(bt1):
    assert bt1.center_of_beams_dist == [295 / 2, (295 + 540 / 2)]


def test_axes_dist(bt1):
    axd = [0, 295, 835]
    assert bt1.axes_dist == axd


def test_axes_dim_points(bt1):
    x1, x2, x3 = 0, 295, 295 + 540
    y2 = bt1.base_dim
    adp = [
        [(x1, y2), (x2, y2)],
        [(x2, y2), (x3, y2)],
    ]
    assert bt1.axes_dim_points == adp


def test_top_polylines_points(bt1, b1, b2):
    tpps = []
    tpps.append(b1.top_polyline_points)
    tpps.append(b2.top_polyline_points)
    assert bt1.top_polylines_points == tpps


def test_bot_polylines_points(bt1, b1, b2):
    bpps = []
    bpps.append(b1.bot_polyline_points)
    bpps.append(b2.bot_polyline_points)
    assert bt1.bot_polylines_points == bpps


def test_stirrups_points(bt1, b1, b2):
    sp = []
    sp.append(b1.stirrup_points)
    sp.append(b2.stirrup_points)
    assert bt1.stirrups_points == sp


def test_edges_polyline_points(bt1, b1, b2):
    epps = []
    epps.append(b1.left_edge_polyline)
    epps.append(b2.right_edge_polyline)
    assert bt1.edges_polyline_points == epps


def test_top_main_rebar_points(bt1):
    tmrp = ((-16.5, -8),
            (-16.5, -2),
            (849, -2),
            (849, -8))
    assert bt1.top_main_rebar_points == tmrp


def test_bot_main_rebar_points(bt1):
    bmrp = ((-16.5, -32),
            (-16.5, -38),
            (849, -38),
            (849, -32))
    assert bt1.bot_main_rebar_points == bmrp


def test_center_of_axis_circle_points(bt1):
    assert hasattr(bt1, 'center_of_axis_circle_points')
    # coacps = ((0, 48), (295, 48), (835, 48))
    # assert bt1.center_of_axis_circle_points == coacps


def test_axes_text(bt1):
    at = ['A1', 'B1', 'C1']
    assert bt1.axes_text == at


def test_top_add_rebar_points(bt1):
    pass


def test_top_add_rebars(bt1):
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
    _tars = bt1.top_add_rebars
    for i in range(3):
        assert np.allclose(_tars[i], tars[i], rtol=.1)


def test_rebar_leader_points(bt1):
    xs = bt1.axes_dist
    y1, y2 = -3.4, 26.6
    for x, _rebar in zip(xs, bt1._top_add_rebars):
        x1 = x - bt1.leader_offcet
        x2 = x1 - bt1.leader_dx
        rlpts = ((x1, y1), (x1, y2), (x2, y2))
        assert np.allclose(rlpts, bt1.rebar_leader_points(_rebar), rtol=.1)


def test_rebar_target_point(bt1):
    xs = bt1.axes_dist
    for x, _rebar in zip(xs, bt1._top_add_rebars):
        _x = x - bt1.leader_offcet
        assert bt1.rebar_target_point(_rebar) == Point(_x, -3.4)


def test_stirrups_dist(bt1):
    assert bt1.stirrups_dist == [[240], [85, 317.5, 85]]


def test_stirrups_count(bt1):
    assert bt1.stirrups_count == [[29], [11, 18, 11]]


def test_stirrups_text(bt1):
    st = ['29~8@8.5', '11~8@8.5', '18~8@17', '11~8@8.5']
    assert bt1.stirrups_text == st


# def test_leader_points(bt1):
#     lpts = [(21.8, -3.4), (21.8, 26.6), (-50.22, 26.6)]
#     assert np.allclose(lpts, bt1.leaders_points())
