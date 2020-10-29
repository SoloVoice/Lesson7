class Cell:
    def __init__(self, cell_numbers):
        self.cell_numbers = cell_numbers

    def __add__(self, other):
        print(f"В результате сложения получается клетка с {self.cell_numbers + other.cell_numbers} ячейками")
        self.make_order(self.cell_numbers + other.cell_numbers)

    def __sub__(self, other):
        if self.cell_numbers - other.cell_numbers <= 0:
            print(f"Вычитание клеток даст отрицательный результат и поэтому это 'харам!'")
        else:
            print(f"в результате вычитания получается клетка с {self.cell_numbers - other.cell_numbers} ячейками")
            self.make_order(self.cell_numbers - other.cell_numbers)

    def __mul__(self, other):
        print(f"В результате умножения получается клетка с {self.cell_numbers * other.cell_numbers} ячейками")
        self.make_order(self.cell_numbers * other.cell_numbers)

    def __truediv__(self, other):
        print(f"В результате деления получается клетка с {self.cell_numbers // other.cell_numbers} ячейками")
        self.make_order(self.cell_numbers // other.cell_numbers)

    def make_order(self, overall_cell, rows=10):
        rows = rows
        row = str()
        count_sup = overall_cell
        count_sub = 0
        while count_sup > 0:
            if count_sub == rows:
                row += "\n"
                count_sub = 0
            else:
                row += "*"
                count_sub += 1
                count_sup -= 1
        print(row)


a = Cell(10)
b = Cell(3)
a + b
a - b
a * b
a / b
