import blankboard

class Board(list):
    def __init__(self, **kwargs):
        super().__init__(self.load_data(**kwargs))
        self.size = len(self)
        self.solved = False
        self.original = [[self[r][c] > 0 for c in range(self.size)] for r in range(self.size)] 
        self.valid = [[True for i in range(self.size)] for j in range(self.size)]

    def load_data(self, **kwargs):
        if kwargs['type'] == 'file':
            with open(kwargs['data']) as f:
              sudokuSorokKiolvasva = f.readlines()
              sudokuSorok = []
              for sor in sudokuSorokKiolvasva:
                aktualisSudokuSorElemei = []
                sor = sor.strip()
                oszlopokAzAktualisSorban = sor.split(" ")
                for elem in oszlopokAzAktualisSorban:
                  aktualisSudokuSorElemei.append(int(elem))
                sudokuSorok.append(aktualisSudokuSorElemei)
              return sudokuSorok
        elif kwargs['type'] == 'list':
            return kwargs['data']

    def check_row(self, row, col):
        for c in range(self.size):
          if c != col and self[row][col] == self[row][c]:
            return False
        return True

    def check_col(self, row, col):
        for r in range(self.size):
          if r != row and self[row][col] == self[r][col]:
            return False
        return True

    def check_sub(self, row, col):
        pass 
        return True

    def check_board(self):
        self.valid = [[True for i in range(self.size)] for j in range(self.size)]
        for r in range(self.size):
            for c in range(self.size):
                self.valid[r][c] = self.check_row(r, c) and self.check_col(r, c) and self.check_sub(r, c) 
        

    def __str__(self):
      board = blankboard.blankboard()
      for row in self:
        for data in row:
          if data > 0:
            board = board.replace('_', str(data), 1)
          else:
            board = board.replace('_', ' ', 1)
      return board
      

board = Board(type = 'file', data = 'boards/001.txt')
print(board)