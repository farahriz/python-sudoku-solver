class Grid:
  def __init__(self):
    self.board = [
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
  
  def print(self):
    for row in self.board:
      print(row)
    print()
  
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