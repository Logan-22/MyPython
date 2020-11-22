class Vestigium:
    def __init__(self, test_case):
        self.__matrix = []
        self.row, self.trace, self.rep_row, self.rep_col, self.temp, self.rep = None, 0, 0, 0, [], []
        self.test_case = test_case
        self.N = int(input())
        self.get_input(self.N)
        self.trace_finder()
        self.latin_square_checker(self.__matrix)
        self.column()
        self.latin_square_checker(self.temp)

    def get_input(self, n):
        for _ in range(n):
            self.row = input().split(" ")
            self.row = list(map(int, self.row))
            self.__matrix.extend([self.row])

    def print_matrix(self):
        print(self.__matrix)

    def trace_finder(self):
        for _ in range(self.N):
            self.trace += self.__matrix[_][_]

    def latin_square_checker(self, temp_list):
        self.rep_row = 0
        for row in temp_list:
            hash_list = [x for x in range(1, self.N+1)]
            for col in row:
                if col in hash_list:
                    hash_list.remove(col)
                else:
                    self.rep_row += 1
                    break
        self.rep.append(self.rep_row)

    def column(self):
        for i in range(self.N):
            self.temp.append([row[i] for row in self.__matrix])


test_cases = int(input())
my_matrix = [Vestigium(_) for _ in range(1, test_cases+1)]
for _ in range(1, test_cases+1):
    print(f'Case #_: {my_matrix[_-1].trace} {my_matrix[_-1].rep[0]} {my_matrix[_-1].rep[1]}')
