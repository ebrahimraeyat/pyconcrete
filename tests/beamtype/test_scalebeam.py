# import pytest
# from pyconcrete.beamtype import scalebeam as sb

# horizontal = 100
# vertical = 20


# @pytest.fixture
# def _beam():
#     '''
#     Beam with two column at bottom and top in left and right
#     and 3 state stirrup, first, middle and last
#     '''
#     b1 = sb.ScaleBeam(horizontal=horizontal,
#                       vertical=vertical,
#                       length=485,
#                       width=40,
#                       height=45,
#                       columns_width=dict(
#                           bot=dict(left=50, right=40,),
#                           top=dict(left=40, right=35,),
#                       ),
#                       stirrup_len=[85, 85],
#                       )
#     return b1


# @pytest.fixture
# def _beam_with_uniform_stirrup():
#     b2 = sb.ScaleBeam(horizontal=horizontal,
#                       vertical=vertical,
#                       length=485,
#                       width=40,
#                       height=45,
#                       columns_width=dict(
#                           bot=dict(left=50, right=40,),
#                           top=dict(left=40, right=35,),
#                       ),
#                       stirrup_len=None,
#                       )
#     return b2


# @pytest.fixture
# def _b3():
#     b3 = sb.ScaleBeam(horizontal=horizontal,
#                       vertical=vertical,
#                       length=485,
#                       width=40,
#                       height=45,
#                       columns_width=dict(
#                           bot=dict(left=0, right=0,),
#                           top=dict(left=0, right=0,),
#                       ),
#                       stirrup_len=None,
#                       )
#     return b3


# @pytest.fixture
# def beam_without_column():
#     beam = sb.ScaleBeam(horizontal=horizontal,
#                         vertical=vertical,
#                         length=485,
#                         width=40,
#                         height=45,
#                         columns_width=dict(
#                             bot=dict(left=50, right=40,),
#                             top=dict(left=0, right=0,),
#                         ),
#                         stirrup_len=None,
#                         is_first=True,
#                         is_last=True,
#                         )
#     return beam


# @pytest.fixture
# def move_beam():
#     b1 = sb.ScaleBeam(horizontal=horizontal,
#                       vertical=vertical,
#                       length=485,
#                       width=40,
#                       height=45,
#                       columns_width=dict(
#                           bot=dict(left=50, right=40,),
#                           top=dict(left=40, right=35,),
#                       ),
#                       stirrup_len=[85, 85],
#                       dx=295,
#                       )
#     return b1


# def test_beam_attribute(_beam):
#     assert hasattr(_beam, 'length')
#     assert hasattr(_beam, 'width')
#     assert hasattr(_beam, 'height')
#     assert hasattr(_beam, 'columns_width')
#     assert hasattr(_beam, 'stirrup_len')
#     assert hasattr(_beam, 'dx')
#     assert hasattr(_beam, 'dy')


# # def test_beam_coordinates(_beam):
# #     p1 = (.20, 0)
# #     p2 = (4.675, 0)
# #     p3 = (.25, -2.25)
# #     p4 = (4.65, -2.25)
# #     coordinates = dict(
# #         top=dict(left=p1, right=p2,),
# #         bot=dict(left=p3, right=p4,))
# #     assert _beam.coordinates == coordinates


# # def test_stirrup_3_state(_beam):
# #     stirrups_dist = [.30, 1.15, 3.80, 4.60]
# #     assert _beam.stirrups_dist == stirrups_dist


# # def test_uniform_stirrup(_beam_with_uniform_stirrup):
# #     assert _beam_with_uniform_stirrup.stirrups_dist == [.30, 4.60]


# # def test_stirrup_points(_beam):
# #     y1 = -1.25 / 20
# #     y2 = (-45 + 1.25) / 20
# #     sp = [
# #         [(.30, y1), (.30, y2)],
# #         [(1.15, y1), (1.15, y2)],
# #         [(3.80, y1), (3.80, y2)],
# #         [(4.60, y1), (4.60, y2)],
#     # ]
#     # assert _beam.stirrup_points == sp


# # def test_shape_coordinates_without_columns(_b3):
# #     p1 = (0, 0)
# #     p2 = (4.85, 0)
# #     p3 = (0, -2.25)
# #     p4 = (4.85, -2.25)
# #     coordinates = dict(
# #         top=dict(left=p1, right=p2,),
# #         bot=dict(left=p3, right=p4,)
# #     )

# #     assert _b3.coordinates == coordinates


# # def test_move_beam_eq_(move_beam):
# #     beam = sb.ScaleBeam(horizontal=horizontal,
# #                         vertical=vertical,
# #                         length=485,
# #                         width=40,
# #                         height=45,
# #                         columns_width=dict(
# #                             bot=dict(left=50, right=40,),
# #                             top=dict(left=40, right=35,),
# #                         ),
# #                         stirrup_len=[85, 85],
# #                         )
# #     assert beam == move_beam


# # def test_move_beam_coordinates(move_beam):
# #     p1 = (.20 + 2.95, 0)
# #     p2 = (4.675 + 2.95, 0)
# #     p3 = (.25 + 2.95, -2.25)
# #     p4 = (4.65 + 2.95, -2.25)
# #     coordinates = dict(
# #         top=dict(left=p1, right=p2,),
# #         bot=dict(left=p3, right=p4,)
# #     )
# #     assert move_beam.coordinates == coordinates


# # def test_top_polyline_points(_beam):
# #     tpp = [(.20, 13.75 / 20),
# #            (.20, 0),
# #            (4.675, 0),
# #            (4.675, 13.75 / 20),
# #            ]
# #     assert _beam.top_polyline_points == tpp


# # def test_bot_polyline_points(_beam):
# #     bpp = [(.25, (-45 - 13.75) / 20),
# #            (.25, -45 / 20),
# #            (4.65, -45 / 20),
# #            (4.65, (-45 - 13.75) / 20),
# #            ]
# #     assert _beam.bot_polyline_points == bpp


# # def test_left_edge_polyline(_beam):
# #     lep = [(-.25, (-45 - 13.75) / 20),
# #            (-.25, 13.75 / 20)]
# #     assert _beam.left_edge_polyline == lep


# # def test_right_edge_polyline(_beam):
# #     rep = [(5.05, (-45 - 13.75) / 20),
# #            (5.05, 13.75 / 20)]
# #     assert _beam.right_edge_polyline == rep


# # def test_beam_without_column(beam_without_column):
# #     p1 = (-.25, 0)
# #     p2 = (5.05, 0)
# #     p3 = (.25, -2.25)
# #     p4 = (4.65, -2.25)
# #     coordinates = dict(
# #         top=dict(left=p1, right=p2,),
# #         bot=dict(left=p3, right=p4,))
# #     assert beam_without_column.coordinates == coordinates


# def test_is_first(_beam):
#     assert _beam.is_first == False


# def test_is_last(_beam):
#     assert _beam.is_last == False


# # def test_left_edge_polyline_without_column(beam_without_column):
# #     lep = [(-.25, (-45 - 13.75) / 20),
# #            (-.25, 0)]
# #     assert beam_without_column.left_edge_polyline == lep


# # def test_right_edge_polyline_without_column(beam_without_column):
# #     rep = [(5.05, (-45 - 13.75) / 20),
# #            (5.05, 0)]
# #     assert beam_without_column.right_edge_polyline == rep
