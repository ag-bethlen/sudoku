import blankboard, colors, messages

class Board(list):
    def __init__(self, **kwargs):
        super().__init__(self.load_data(**kwargs))
        self.size = len(self)
        self.solved = False
        self.checking = False
        self.original = [[self[r][c] > 0 for c in range(self.size)]
                         for r in range(self.size)]
        self.valid = [[True for i in range(self.size)]
                      for j in range(self.size)]

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
        if self[row][col] == 0:
            return True
        for c in range(self.size):
            if c != col and self[row][col] == self[row][c]:
                return False
        return True

    def check_col(self, row, col):
        if self[row][col] == 0:
            return True
        for r in range(self.size):
            if r != row and self[row][col] == self[r][col]:
                return False
        return True

    def check_sub(self, row, col):
        if self[row][col] == 0:
            return True
        for r in range((row // 3) * 3, (row // 3) * 3 + 3):
            for c in range((col // 3) * 3, (col // 3) * 3 + 3):                
                if not (r == row and c == col) and self[r][c] == self[row][col]:
                    return False
        return True
          


    def check_board(self):
        self.checking = True
        self.valid = [[True for i in range(self.size)]
                      for j in range(self.size)]
        self.solved = True
        for r in range(self.size):
            for c in range(self.size):
                if self[r][c] == 0:
                    self.solved = False
                if self.check_row(r, c) and self.check_col(
                        r, c) and self.check_sub(r, c):
                    self.valid[r][c] = True
                else:
                    self.valid[r][c] = False
                    self.solved = False
        self.checking = False

    def turn(self, row, col, value):
        if self.original[row][col]:
            return 11  # 11-es hiba, a mez?? nem m??dos??that??
        else:
            self[row][col] = value
            self.check_board()
            return 0  # HF: minden f??ggv??ny adjon vissza 0-t, ha minden ok

    def __str__(self):
        board = blankboard.blankboard()
        for row in range(self.size):
            for col in range(self.size):
                board = board.replace(' _ ', self.display(row, col), 1)
        return board

    def display(self, row, col):
        if self[row][col] == 0:
            return '   '
        else:
            if not self.valid[row][col]:
                return colors.PURPLE + ' ' + str(self[row][col]) + ' ' + colors.END
            elif self.original[row][col]:
                return colors.BLUE + ' ' + str(self[row][col]) + ' ' + colors.END
            else:
                return ' ' + str(self[row][col]) + ' '


board = Board(type='file', data='boards/001.txt')
print(board)
while not board.solved:
    row = int(input(messages.ROW)) - 1   # mert indexek... 
    col = int(input(messages.COL)) - 1
    val = int(input(messages.VAL))
    error = board.turn(row, col, val)
    if error == 11: 
      print(messages.ORIGINAL_FIELD)  # hf: sz??p ??zenet
    print(board)
print('Solved...')