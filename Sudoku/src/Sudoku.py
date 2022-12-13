class Sudoku:

    def __init__(self, grid=None):
        if grid is None:
            self.grid = [[-1] * 9 for i in range(9)]
        else:
            self.grid = grid

    def __str__(self):
        res = ""
        for row in range(9):
            for column in range(9):
                res += str(self.grid[row][column]) if self.grid[row][column] != -1 else "."
                if not (column + 1) % 3 == 0:
                    res += " "
                elif (column + 1) % 3 == 0 and column < 8:
                    res += "|"
            res += "\n-----+-----+-----\n" if (row + 1) % 3 == 0 and row < 8 else "\n"
        return res

    def __copy__(self):
        return Sudoku(self.grid)

    def is_valid(self) -> bool:
        """
        Return True if the sudoku is valid, False otherwise
        """
        found_row = set()
        found_col = set()
        found_3 = set()
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != -1:
                    if (str(i) + str(self.grid[i][j])) in found_row or \
                            (str(j) + str(self.grid[i][j])) in found_col or \
                            (str((i // 3) * 3 + (j // 3)) + str(self.grid[i][j])) in found_3:
                        return False
                    else:
                        found_row.add(str(i) + str(self.grid[i][j]))
                        found_col.add(str(j) + str(self.grid[i][j]))
                        found_3.add(str((i // 3) * 3 + (j // 3)) + str(self.grid[i][j]))
        return True


if __name__ == '__main__':
    sudoku = Sudoku([[5, 3, -1, -1, 7, -1, -1, -1, -1],
                     [6, -1, -1, 1, 9, 5, -1, -1, -1],
                     [-1, 9, 8, -1, -1, -1, -1, 6, -1],
                     [8, -1, -1, -1, 6, -1, -1, -1, 3],
                     [4, -1, -1, 8, -1, 3, -1, -1, 1],
                     [7, -1, -1, -1, 2, -1, -1, -1, 6],
                     [-1, 6, -1, -1, -1, -1, 2, 8, -1],
                     [-1, -1, -1, 4, 1, 9, -1, -1, 5],
                     [-1, -1, -1, -1, 8, -1, -1, 7, 9]])
    print(sudoku)
    print(sudoku.is_valid())
