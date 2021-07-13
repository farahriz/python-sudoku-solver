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
    """Print board without any borders
    """
    for row in self.board:
      print(row)

  def print_board(self):
    """Print the board with borders for each 3x3 in the sudoku grid
    """
    num_rows = len(self.board)
    num_cols = len(self.board[0])
    
    for i in range(num_rows):
      if i % 3 == 0 and i != 0:
        print("- - - - - - - - - - - -")
      
      for j in range(num_cols):
        if j % 3 == 0 and j != 0:
          print(" | ", end="")
        
        if j == 8:
          print(self.board[i][j])
        else:
          number = str(self.board[i][j])
          print("{} ".format(number), end='')

  def set_row(self, row_index, new_row):
    ind = row_index - 1
    self.board[ind] = new_row

  def set_column(self, col_index, new_col):
    ind = col_index - 1
    for i, row in enumerate(self.board):
      row[ind] = new_col[i]

grid = Grid()
grid.print()
grid.print_board()