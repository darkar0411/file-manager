class Grid():

    grid: dict

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.grid = {'row': self.row, 'column': self.column}

print(Grid(0, 0).grid)