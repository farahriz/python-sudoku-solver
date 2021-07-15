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
    # self.board = board
  
  def set_board(self, board):
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
  
  def find_empty(self):
    """Loop through the board and find an empty square.
    Empty squares are designated by 0
    """
    num_rows = len(self.board)
    num_cols = len(self.board[0])

    for i in range(num_rows):
      for j in range(num_cols):
        if self.board[i][j] == 0:
          return (i, j)

  def is_valid(self, num, position):
    """Checks that a number can be used in a grid position by checking if it already appears in the corresponding row, column, or subgrid

    Args:
        num (Int): The number being checked to fit in the space
        position (Tuple): The position of the space in the grid, given by two coordinates (row_number, column_number)

    Returns:
        Boolean: True or False depending on if the number is valid for the space or not
    """

    num_rows = len(self.board)
    num_cols = len(self.board[0])
    
    # Check row for other numbers
    for i in range(num_cols):
      if self.board[position[0]][i] == num and position[1] != i:
        return False

    # Check column for other numbers
    for i in range(num_rows):
      if self.board[i][position[1]] == num and position[0] != i:
        return False
    
    # Check 3z3 subsquare
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y*3 + 3):
      for j in range(box_x * 3, box_x*3 + 3):
        if self.board[i][j] == num and (i, j) != position:
          return False
    
    return True

grid = Grid()
grid.set_board(test_board)
grid.print()
grid.print_board()