import pytest
from pyconcrete import point as p


@pytest.fixture
def p1():
    _p1 = p.Point(2, 3)

    return _p1


@pytest.fixture
def p2():
    _p2 = p.Point(-2, 4)

    return _p2


def test_eq_method(p1, p2):
    assert (p1 == p2) == False


def test_plusx():
    point = p.Point(2, 3)
    point.plusx(2)
    assert point == p.Point(4, 3)


def test_to_tuple(p1):
    assert p1.to_tuple() == (2, 3, 0)


def test_to_xytuple(p1):
    assert p1.to_xytuple() == (2, 3)
