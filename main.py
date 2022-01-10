import blankboard

class Board(list):
    def __init__(self, **kwargs):
        super().__init__(self.load_data(**kwargs))
        self.size = len(self)
        self.solved = False
        self.original = [] # itt folyt.
        self.valid = []


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

board = Board(type = 'file', data = 'boards/001.txt')
print(board)