board = [
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

class Grid:
  def __init__(self):
    self.empty_board = [
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0]
    ]
    self.board = board
  
  def print(self):
    for row in self.board:
      print(row)
    print()
  
  def print_nice_grid(self):
    0 0 0 | 0 0 0 | 0 0 0
    0 0 0 | 0 0 0 | 0 0 0
    0 0 0 | 0 0 0 | 0 0 0
    - - -   - - -   - - -
    0 0 0 | 0 0 0 | 0 0 0
    0 0 0 | 0 0 0 | 0 0 0
    0 0 0 | 0 0 0 | 0 0 0
    - - -   - - -   - - -
    0 0 0 | 0 0 0 | 0 0 0
    0 0 0 | 0 0 0 | 0 0 0
    0 0 0 | 0 0 0 | 0 0 0

    print(neat_grid)

  def set_row(self, row_index, new_row):
    ind = row_index - 1
    self.board[ind] = new_row

  def set_column(self, col_index, new_col):
    ind = col_index - 1
    for i, row in enumerate(self.board):
      row[ind] = new_col[i]

grid = Grid()
grid.print()
grid.set_column(7, [1,2,3,4,5,6,7,8,9])
grid.print()


1. p