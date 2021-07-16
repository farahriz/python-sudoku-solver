import pytest
from grid.grid import Grid

new_grid = Grid()

test_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def test_set_board():
    new_grid.set_board(new_grid.empty_board)
    assert new_grid.board == new_grid.empty_board 

def test_print(capsys):
    new_grid.set_board(test_board)
    new_grid.print()
    captured = capsys.readouterr()
    assert captured.out == test_board

# def test_new_func():
#     assert 4 == 5