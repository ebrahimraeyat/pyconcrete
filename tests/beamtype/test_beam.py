import pytest
from pyconcrete.beamtype import beam as b


@pytest.fixture
def _beam():
  '''
  Beam with two column at bottom and top in left and right
  and 3 state stirrup, first, middle and last
  '''
  b1 = b.Beam(length=485,
              width=40,
              height=45,
              columns_width=dict(
                  bot=dict(left=50, right=40,),
                  top=dict(left=40, right=35,),),
              stirrup_len=[85, 85],
              stirrup_at=[8.5, 17, 8.5],
              stirrup_size=8,
              )
  return b1


@pytest.fixture
def _beam_with_uniform_stirrup():
  b2 = b.Beam(length=485,
              width=40,
              height=45,
              columns_width=dict(
                  bot=dict(left=50, right=40,),
                  top=dict(left=40, right=35,),),
              stirrup_len=None,
              )
  return b2


@pytest.fixture
def _b3():
  b3 = b.Beam(length=485,
              width=40,
              height=45,
              columns_width=dict(
                  bot=dict(left=0, right=0,),
                  top=dict(left=0, right=0,),),
              stirrup_len=None,
              stirrup_at=[8.5],
              stirrup_size=8,
              )
  return b3


@pytest.fixture
def beam_without_column():
  beam = b.Beam(length=485,
                width=40,
                height=45,
                columns_width=dict(
                    bot=dict(left=50, right=40,),
                    top=dict(left=0, right=0,),),
                stirrup_len=None,
                is_first=True,
                is_last=True,
                )
  return beam


@pytest.fixture
def move_beam():
  b1 = b.Beam(length=485,
              width=40,
              height=45,
              columns_width=dict(
                  bot=dict(left=50, right=40,),
                  top=dict(left=40, right=35,),),
              stirrup_len=[85, 85],
              dx=295,
              )
  return b1


def test_beam_attribute(_beam):
  assert hasattr(_beam, 'length')
  assert hasattr(_beam, 'width')
  assert hasattr(_beam, 'height')
  assert hasattr(_beam, 'columns_width')
  assert hasattr(_beam, 'stirrup_len')
  assert hasattr(_beam, 'dx')
  assert hasattr(_beam, 'dy')


def test_beam_coordinates(_beam):
  p1 = (20, 0)
  p2 = (467.5, 0)
  p3 = (25, -45)
  p4 = (465, -45)
  coordinates = dict(
      top=dict(left=p1, right=p2,),
      bot=dict(left=p3, right=p4,))
  assert _beam.coordinates == coordinates


def test_stirrup_3_state(_beam):
  stirrups_x = [30, 115, 375, 460]
  assert _beam.stirrups_x == stirrups_x


def test_uniform_stirrup(_beam_with_uniform_stirrup):
  assert _beam_with_uniform_stirrup.stirrups_x == [30, 460]


def test_stirrup_points(_beam):
  y1 = -1.25
  y2 = -45 + 1.25
  sp = [
      [(30, y1), (30, y2)],
      [(115, y1), (115, y2)],
      [(375, y1), (375, y2)],
      [(460, y1), (460, y2)],
  ]
  assert _beam.stirrup_points == sp


def test_shape_coordinates_without_columns(_b3):
  p1 = (0, 0)
  p2 = (485, 0)
  p3 = (0, -45)
  p4 = (485, -45)
  coordinates = dict(
      top=dict(left=p1, right=p2,),
      bot=dict(left=p3, right=p4,))
  assert _b3.coordinates == coordinates


def test_move_beam_eq_(move_beam):
  beam = b.Beam(length=485,
                width=40,
                height=45,
                columns_width=dict(
                    bot=dict(left=50, right=40,),
                    top=dict(left=40, right=35,),),
                stirrup_len=[85, 85],
                )
  assert beam == move_beam


def test_move_beam_coordinates(move_beam):
  p1 = (20 + 295, 0)
  p2 = (467.5 + 295, 0)
  p3 = (25 + 295, -45)
  p4 = (465 + 295, -45)
  coordinates = dict(
      top=dict(left=p1, right=p2,),
      bot=dict(left=p3, right=p4,))
  assert move_beam.coordinates == coordinates


def test_top_polyline_points(_beam):
  tpp = [(20, 13.75),
         (20, 0),
         (467.5, 0),
         (467.5, 13.75),
         ]
  assert _beam.top_polyline_points == tpp


def test_bot_polyline_points(_beam):
  bpp = [(25, -45 - 13.75),
         (25, -45),
         (465, -45),
         (465, -45 - 13.75),
         ]
  assert _beam.bot_polyline_points == bpp


def test_left_edge_polyline(_beam):
  lep = [(-25, -45 - 13.75),
         (-25, 13.75)]
  assert _beam.left_edge_polyline == lep


def test_right_edge_polyline(_beam):
  rep = [(505, -45 - 13.75),
         (505, 13.75)]
  assert _beam.right_edge_polyline == rep


def test_beam_without_column(beam_without_column):
  p1 = (-25, 0)
  p2 = (505, 0)
  p3 = (25, -45)
  p4 = (465, -45)
  coordinates = dict(
      top=dict(left=p1, right=p2,),
      bot=dict(left=p3, right=p4,))
  assert beam_without_column.coordinates == coordinates


def test_is_first(_beam):
  assert _beam.is_first == False


def test_is_last(_beam):
  assert _beam.is_last == False


def test_left_edge_polyline_without_column(beam_without_column):
  lep = [(-25, -45 - 13.75),
         (-25, 0)]
  assert beam_without_column.left_edge_polyline == lep


def test_right_edge_polyline_without_column(beam_without_column):
  rep = [(505, -45 - 13.75),
         (505, 0)]
  assert beam_without_column.right_edge_polyline == rep


def test_stirrup_dim_points(_beam, _beam_with_uniform_stirrup):
  y = -22.5
  sdps = [
      [(30, y), (115, y)],
      [(115, y), (375, y)],
      [(375, y), (460, y)]
  ]
  assert _beam.stirrup_dim_points == sdps
  assert _beam_with_uniform_stirrup.stirrup_dim_points == [[(30, y), (460, y)]]


def test_uniform_stirrup_dim_points(_beam_with_uniform_stirrup):
  y = -22.5
  sdps = [[(30, y), (460, y)]]
  assert _beam_with_uniform_stirrup.stirrup_dim_points == sdps


def test_stirrups_len(_beam):
  assert _beam.stirrups_len == [85, 260, 85]


def test_stirrup_counts(_beam):
  assert _beam.stirrup_counts == [11, 15, 11]


def test_stirrup_text(_beam):
  st = ['11~8@8.5', '15~8@17', '11~8@8.5']
  assert _beam.stirrup_text == st
# def test_len_stirrup_prop(_beam, _b3):
#   for beam in [_beam, _b3]:
#     l1 = len(beam.stirrup_at)
#     l
#     assert l1 == l2
