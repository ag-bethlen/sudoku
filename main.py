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
        pass
        return True

    def check_col(self, row, col):
        pass

    def check_sub(self, row, col):
        pass

    def check_board(self):
        pass


# board = Board(type = 'list', data =[[7, 8, 2, 1, 3, 0, 4, 6, 9], [3, 7, 6, 4, 8, 9, 2, 1, 5], [9, 4, 1, 6, 5, 0, 0, 8, 0], [6, 2, 5, 3, 7, 4, 1, 9, 8], [8, 3, 7, 9, 0, 1, 6, 5, 4], [4, 1, 9, 5, 6, 0, 7, 0, 0], [7, 9, 0, 0, 1, 6, 5, 4, 0], [2, 6, 3, 0, 4, 5, 9, 7, 1], [1, 5, 4, 7, 9, 0, 8, 0, 6]])

board = Board(type = 'file', data = 'boards/001.txt')
print(board)