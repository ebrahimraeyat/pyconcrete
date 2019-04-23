import pytest

from pyconcrete import rebar


@pytest.fixture
def r1():
    r = rebar.Rebar(
        length=5,
        diameter=20,
        count=1,
        insert=(0, 0))
    return r


@pytest.fixture
def lr1():
    r = rebar.LRebar(
        length=5,
        diameter=20,
        count=2,
        insert=(10, 20),
        v_align='top',
        h_align='left')
    return r


@pytest.fixture
def ur1():
    r = rebar.URebar(
        length=200,
        diameter=16,
        count=4,
        insert=(0, 0),
        v_align='bot')
    return r


def test_length(r1):
    assert r1.length == 5


def test_diameter(r1):
    assert r1.diameter == 20


def test_count(r1):
    assert r1.count == 1


def test_insert(r1):
    assert r1.insert == (0, 0)


def test_points(r1):
    pts = [(0, 0), (5, 0)]
    assert r1.points() == pts


def test_length_L(lr1):
    assert lr1.length == 5


def test_diameter_l(lr1):
    assert lr1.diameter == 20


def test_count_l(lr1):
    assert lr1.count == 2


def test_insert_l(lr1):
    assert lr1.insert == (10, 20)


def test_points_l(lr1):
    pts = [(10, 14), (10, 20), (15, 20)]
    assert lr1.points() == pts


def test_points_u(ur1):
    pts = [(0, 6), (0, 0), (200, 0), (200, 6)]
    assert ur1.points() == pts


def test_points_along(r1, lr1, ur1):
    assert r1.points_along() == [(1.25, 0), (2.5, 0), (3.75, 0)]
    assert lr1.points_along() == [(11.25, 20), (12.5, 20), (13.75, 20)]
    assert ur1.points_along() == [(50, 0), (100, 0), (150, 0)]


def test_text(r1, lr1, ur1):
    assert r1.text == '1~20'
    assert lr1.text == '2~20'
    assert ur1.text == '4~16'
