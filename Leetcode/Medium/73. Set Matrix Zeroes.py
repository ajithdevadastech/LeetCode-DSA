class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        firstRowHasZero = False
        firstColHasZero = False

        rows = len(matrix)
        cols = len(matrix[0])

        #set 1st row and 1st column zero presence boolean

        r = 0
        c = cols

        i = 0
        while i < cols:
            if matrix[r][i] == 0:
                firstRowHasZero = True
                break
            i = i + 1

        r =  rows
        c = 0

        i = 0
        while i < rows:
            if matrix[i][c] == 0:
                firstColHasZero = True
                break
            i = i + 1

        i = 0
        j = 0

        #set zeroes on the 1st row and col of zeroes
        while i < rows:
            while j < cols:
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                j = j + 1
            j = 0
            i = i + 1

        #loop through first row set all zeroes

        i = 0
        j = 1

        while j < cols:
            if matrix[i][j] == 0:
                a = 0
                while a < rows:
                    matrix[a][j] = 0
                    a = a + 1
            j = j + 1

        #loop through first col set all zeroes

        i = 1
        j = 0

        while i < rows:
            if matrix[i][j] == 0:
                a = 0
                while a < cols:
                    matrix[i][a] = 0
                    a = a + 1
            i = i + 1

        #make first row and col zeroes based on boolean

        if firstRowHasZero:
            j = 0
            while j < cols:
                matrix[0][j] = 0
                j = j + 1


        if firstColHasZero:
            i = 0
            while i < rows:
                matrix[i][0] = 0
                i = i + 1

        return matrix

o = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(o.setZeroes(matrix))






