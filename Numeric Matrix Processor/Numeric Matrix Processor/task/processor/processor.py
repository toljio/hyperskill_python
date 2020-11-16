class Matrix:
    def __init__(self, matrix=()):
        self.matrix = matrix

    def __str__(self):
        return "\n".join(" ".join(str(x) for x in row) for row in self.matrix)

    def __add__(self, other):
        a = self.matrix
        b = other.matrix
        if len(a) != len(b):
            raise ValueError
        result = []
        for i in range(len(a)):
            result.append([])
            for j in range(len(a[i])):
                result[i].append(float(a[i][j]) + float(b[i][j]))
        return Matrix(result)

    def __mul__(self, other):
        result = []
        a = self.matrix
        if isinstance(other, str):
            for i in range(len(a)):
                result.append([])
                for j in range(len(a[i])):
                    result[i].append(int(a[i][j]) * int(other))
        else:
            b = other.matrix
            if len(a[0]) != len(b):
                raise ValueError
            for i in range(len(a)):
                result.append([])
                for k in range(len(b[0])):
                    s = 0
                    result.append([])
                    for j in range(len(a[i])):
                        s += float(a[i][j]) * float(b[j][k])
                    result[i].append(s)
        return Matrix(result)

    def transpose(self, ttype):
        result = []
        if ttype == 1:
            for j in range(len(self.matrix[0])):
                result.append([])
                for i in range(len(self.matrix)):
                    result[j].append(self.matrix[i][j])
        elif ttype == 2:
            for j in range(len(self.matrix[0]), 0, -1):
                result.append([])
                for i in range(len(self.matrix), 0, -1):
                    result[len(self.matrix[0]) - j].append(self.matrix[i - 1][j - 1])
        if ttype == 3:
            for i in range(len(self.matrix)):
                result.append([])
                for j in range(len(self.matrix[i]), 0, -1):
                    result[i].append(self.matrix[i][j - 1])
        if ttype == 4:
            for i in range(len(self.matrix), 0, -1):
                result.append([])
                for j in range(len(self.matrix[i - 1])):
                    result[len(self.matrix) - i].append(self.matrix[i - 1][j])
        return Matrix(result)

    @classmethod
    def factory(cls, name=""):
        matrix_len = input(f'Enter size of {name} matrix:').split()
        print(f'Enter {name} matrix:')
        result = []
        for i in range(int(matrix_len[0])):
            result.append(input().split())
            if len(result[i]) != int(matrix_len[1]):
                raise TypeError
        return Matrix(result)


class MatrixCalculator:
    def __init__(self):
        self.finish = False

    def start(self):
        while not self.finish:
            print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit""")
            try:
                a = self.execute(input("Your choice:"))
                print("The result is:", a, sep="\n")
            except (ValueError, TypeError):
                print("ERROR.")

    def execute(self, cmd):
        if cmd == "0":
            self.finish = True
            return
        elif cmd == "1":
            m1 = Matrix.factory("first")
            m2 = Matrix.factory("second")
            return m1 + m2
        elif cmd == "2":
            m = Matrix.factory()
            c = input("Enter constant:")
            return m * c
        elif cmd == "3":
            m1 = Matrix.factory("first")
            m2 = Matrix.factory("second")
            return m1 * m2
        elif cmd == "4":
            n = input("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line\n")
            m = Matrix.factory()
            return m.transpose(int(n))
        else:
            return False
        return True

    def matrix_prompt(self, name=""):
        matrix_len = input(f'Enter size of {name} matrix:').split()
        print(f'Enter {name} matrix:')
        result = []
        for i in range(int(matrix_len[0])):
            result.append(input().split())
            if len(result[i]) != int(matrix_len[1]):
                print("ERROR input")
        return result


mc = MatrixCalculator()
mc.start()
