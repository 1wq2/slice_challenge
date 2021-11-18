import pytest
from pizzabot import parser, get_route


def test_parser_no_bracket():
    with pytest.raises(ValueError, match='bracket'):
        parser("5x5 2,3) 4, 5)")


def test_parser_no_floats():
    with pytest.raises(ValueError, match='floats'):
        parser("4.1x3.2(2,2)")


def test_parser_grid_2_values_for_axis():
    with pytest.raises(ValueError, match='2 values'):
        parser("5x(1,2) (3,3)")
        parser("5x5 1,2) (3,3)")


def test_parser_non_positive_grid():
    with pytest.raises(ValueError, match='positive'):
        parser("-5x0 (1, 3) (4, 4)")


def test_parser_neg_coords():
    with pytest.raises(ValueError, match='(?=.*non-negative)(?=.*coordinates)'):
        parser("5x5 (-1, 3) (4, -4)")


def test_parser_no_points():
    with pytest.raises(ValueError, match='At least one'):
        parser("5x5 (1,)")


def test_parser_odd_number_of_coords():
    with pytest.raises(ValueError, match='must have 2'):
        parser("5x5 (1, 3) (4) (1, 2)")


def test_parser_coord_value_exceeds_grid():
    with pytest.raises(ValueError, match='cannot exceed'):
        parser("5x5 (1, 3) (4, 40)")


def test_bot_origin_delivery():
    crds = parser("5x5 (0,0)")
    assert get_route(crds) == 'D'


def test_bot_sample_data():
    crds = parser("5x5 (1, 3) (4, 4)")
    assert get_route(crds) == 'ENNNDEEEND'


def test_bot_samble_broken_data():
    crds = parser("5 x  5 (1, 3  4, 4")
    assert get_route(crds) == 'ENNNDEEEND'


def test_bot_main_challenge():
    """ Test for task's main input data """
    crds = parser("5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)")
    assert get_route(crds) == 'DENNNDEEENDSSDWWWWSDEEENDWNDEESSD'
