import pytest
from grid.grid import Grid

new_grid = Grid()


def test_set_board():
    new_grid.set_board(new_grid.empty_board)
    assert new_grid.board == new_grid.empty_board 

# def test_new_func():
#     assert 4 == 5