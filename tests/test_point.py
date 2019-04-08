import pytest
from pyconcrete import point as p


@pytest.fixture
def p1():
    p1 = p.Point(2, 3)
    return p1


@pytest.fixture
def p2():
    p2 = p.Point(-2, 4)
    return p2


def test_eq_method(p1, p2):
    assert (p1 == p2) == False


def test_plusx(p1):
    point = p1.plusx(2)
    assert point == p.Point(4, 3)


def test_plusy(p1):
    point = p1.plusy(2)
    assert point == p.Point(2, 5)


def test_tuple(p1):
    assert tuple(p1) == (2, 3)


def test_scale():
    p1 = p.Point(2, 30)
    p1.scale(h=.5, v=.1)
    assert p1 == p.Point(1, 3)


def test__add__(p1, p2):
    point = p1 + p2
    assert point == p.Point(0, 7)


def test__sub__(p1, p2):
    point = p1 - p2
    assert point == p.Point(4, -1)


def test_multiple_point(p1, p2):
    p3 = p1 + p2
    assert sum([p1, p2, p3]) == p.Point(0, 14)
