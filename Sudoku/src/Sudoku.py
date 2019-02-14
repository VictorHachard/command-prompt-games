class Sudoku:

    def __init__(self):
        self.list = [[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9]
        self.const1 = {0:0,1:0,2:0,3:1,4:1,5:1,6:2,7:2,8:2}
        self.const2 = {0:0,1:3,2:6}

    '''
    Print the sudoku
    '''
    def toString(self):
        res = ""
        for row in range(9):
            for column in range(9):
                res += str(self.list[row][column]) if self.list[row][column] != -1 else "."
                if (not (column+1)%3 == 0):
                    res += " "
                elif ((column+1)%3 == 0 and column < 8):
                    res += "|"
            res += "\n-----+-----+-----\n" if (row+1)%3 == 0 and row < 8 else "\n"
        print(res)

    '''
    Print the sudoku
    '''
    def toString(self, list):
        res = ""
        for row in range(9):
            for column in range(9):
                res += str(list[row][column]) if list[row][column] != -1 else "."
                if (not (column+1)%3 == 0):
                    res += " "
                elif ((column+1)%3 == 0 and column < 8):
                    res += "|"
            res += "\n-----+-----+-----\n" if (row+1)%3 == 0 and row < 8 else "\n"
        print(res)

    '''
    Add a number to the sudoku at the row, column
    arg row => the index of the row between 0 and 8
    arg column => the index of the column between 0 and 8
    arg element => the number to add
    '''
    def add(self, row, column, element):
        if (column < 0 or column >= 9 or row < 0 or row >= 9):
            print("the number of column or row you enter is not correct " + str(column) + ", " + str(row) + ", enter a number between 0 and 8")
            return
        columnBool = not element in self.getColumn(self.list, column)
        rowBool = not element in self.getRow(self.list, row)
        if (columnBool and rowBool):
            self.list[row][column] = element
        else:
            print("can't add " + str(element)  + " in row " + str(row) + ", column " + str(column))

    '''
    Remove a number of the sudoku at the row, column
    arg row => the index of the row between 0 and 8
    arg column => the index of the column between 0 and 8
    arg element => the number to remove
    '''
    def remove(self, row, column):
        if (column < 0 or column >= 9 or row < 0 or row >= 9):
            print("the number of column or row you enter is not correct " + str(column) + ", " + str(row) + ", enter a number between 0 and 8")
            return
        self.list[row][column] = -1

    '''
    Return a new list of a row of the sudoku
    arg list => the sudoku
    arg column => the index of the column between 0 and 8
    return => a 9 length list
    '''
    def getRow(self, list, row):
        if (row < 0 or row >= 9):
            print("the number of row you enter is not correct " + str(row)  + ", enter a number between 0 and 8")
            return
        return list[row]

    '''
    Return a new list of a column of the sudoku
    arg list => the sudoku
    arg column => the index of the column between 0 and 8
    return => a 9 length list
    '''
    def getColumn(self, list, column):
        if (column < 0 or column >= 9):
            print("the number of column you enter is not correct " + str(column)  + ", enter a number between 0 and 8")
            return
        res = [-1]*9
        for i in range(9):
            res[i] = list[i][column]
        return res

    '''
    Return a new list of a cell of the sudoku
    arg list => the sudoku
    arg row => the index of the row between 0 and 2
    arg column => the index of the column between 0 and 2
    return => a 9 length list
    '''
    def getCell(self, list, row, column):
        res = [-1]*9
        offsetRow = self.const2.get(row, -1)
        offsetColumn = self.const2.get(column, -1)
        if (offsetRow == -1):
            print("the number of row you enter is not correct " + str(row)  + ", enter a number between 0 and 2")
            return
        if (offsetColumn == -1):
            print("the number of column you enter is not correct " + str(column)  + ", enter a number between 0 and 2")
            return
        i = 0
        for row in range(3):
            for column in range(3):
                res[i] = list[row+offsetRow][column+offsetColumn]
                i += 1
        return res

    '''
    Return a copy of the sudoku
    arg list => the sudoku
    return => a 2D 9*9 list
    '''
    def copy(self, list):
        res = [[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9,[-1]*9]
        for row in range(9):
            for column in range(9):
                res[row][column] = list[row][column];
        return res

    '''
    Return True if the sudoku is valide, False the otherwise
    arg list => the sudoku to verify
    return => a boolean
    '''
    def isValid(self, list):
        for row in range(9):
            for column in range(9):
                element = list[row][column]
                if (element == -1):
                    return False
                list[row][column] = -1
                bool = not self.isValideToPlace(list, element, row, column)
                list[row][column] = element
                if (bool):
                    return False
        return True

    '''
    Return True if the element can be place, False the otherwise
    arg list => the sudoku to verify
    arg list => the element to place
    arg row => the index of the row between 0 and 8
    arg column => the index of the column between 0 and 8
    return => a boolean
    '''
    def isValideToPlace(self, list, element, row, column):
        columnOccurrences = self.getColumn(list, column).count(element)
        rowOccurrences = self.getRow(list, row).count(element)
        cellOccurrences = self.getCell(list, self.const1.get(row, -1), self.const1.get(column, -1)).count(element)
        if (columnOccurrences >= 1 or rowOccurrences >= 1 or cellOccurrences >= 1):
            return False
        return True

    '''
    Return the list with shure completed value
    arg list => the sudoku to resolve
    return => a 2D 9*9 list
    '''
    def preSolve(self, list):
        for row in range(9):
            for column in range(9):
                if (list[row][column] == -1):
                    nbr = 0
                    valueToPlace = 0
                    for value in range(1,10):
                        if (self.isValideToPlace(list, value, row, column)):
                            nbr += 1
                            valueToPlace = value
                    if (nbr == 1):
                        list[row][column] = valueToPlace
        return list

    '''
    NOT WORKING
    Return
    arg list => the sudoku to resolve
    return =>
    '''
    def solve(self, list):
        listToDestroy = self.copy(list)
        #for i in range(10):
            #listToDestroy = self.preSolve(listToDestroy) #Place number where there is juste one possibility
        for row in range(9):
            for column in range(9):
                if (listToDestroy[row][column] == -1):
                    for value in range(1,10):
                        if (self.isValideToPlace(list, value, row, column)):
                            boll = True
                            cellTab = self.getCell(list, self.const1.get(row, -1), self.const1.get(column, 0))
                            for cell in range(len(cellTab)):
                                if (cellTab[cell] == -1):
                                    columnOccurrences = self.getColumn(list, column).count(value)
                                    rowOccurrences = self.getRow(list, row).count(value)
                                    if (columnOccurrences >= 1 or rowOccurrences >= 1):
                                        boll =+ True
                                    else:
                                        boll =+ False
                            if (boll):
                                listToDestroy[row][column] = value
                                break
        return listToDestroy

if __name__ == '__main__':

    test = Sudoku()
    #init
    test.add(0,1,4)
    test.add(0,2,2)
    test.add(0,4,3)
    test.add(0,7,5)
    test.add(0,8,1)
    test.add(1,2,8)
    test.add(1,3,1)
    test.add(1,4,5)
    test.add(1,8,7)
    test.add(2,0,3)
    test.add(2,1,1)
    test.add(2,6,8)
    test.add(2,7,2)
    test.add(2,8,6)
    test.add(3,5,5)
    test.add(3,6,7)
    test.add(4,0,8)
    test.add(4,1,5)
    test.add(4,7,1)
    test.add(4,8,3)
    test.add(5,2,4)
    test.add(5,3,2)
    test.add(6,0,5)
    test.add(6,1,6)
    test.add(6,2,3)
    test.add(6,7,7)
    test.add(6,8,9)
    test.add(7,0,9)
    test.add(7,4,4)
    test.add(7,5,7)
    test.add(7,6,5)
    test.add(8,0,4)
    test.add(8,1,2)
    test.add(8,4,9)
    test.add(8,6,1)
    test.add(8,7,3)
    test.toString(test.list)

    '''while True:
        x = input("row:")
        y = input("col:")
        z = input("elem:")
        test.add(int(x),int(y),int(z))
        test.toString()'''

    test.toString(test.preSolve(test.list))
    test.toString(test.preSolve(test.list))
    test.toString(test.preSolve(test.list))
    test.toString(test.preSolve(test.list))
    print(test.isValid(test.list))
