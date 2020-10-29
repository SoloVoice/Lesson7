class Matrix:
    def __init__(self, mtx):
        self.mtx = mtx

    def __str__(self):
        a1 = ""
        for i in self.mtx:
            b1 = []
            for j in i:
                b1.append(str(j))
            a1 += " ".join(b1) + "\n"
        return a1

    def __add__(self, other):
        mtx1 = self.mtx
        mtx2 = other.mtx
        if len(mtx1) == len(mtx2):
            c = []
            for x, y in zip(mtx1, mtx2):
                tr = []
                for z, w in zip(x, y):
                    tr.append(z + w)
                c.append(tr)
            a1 = ""
            for i in c:
                b1 = []
                for j in i:
                    b1.append(str(j))
                a1 += " ".join(b1) + "\n"
            return a1
        else:
            return f"Матрицы разной длинны не могут быть сложены"


a = Matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
b = Matrix([[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]])
c = Matrix([[56, 13, 184, 139, 201], [221, 232, 423, 124, 425], [256, 277, 298, 269, 330]])
print(a)
print(b)
print(a + c)
