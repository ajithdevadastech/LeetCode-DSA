class Solution(object):
    def totalNQueens(self, n):

        def blockCells (pos,matrix, prev, curr):
            r = pos[0]
            c = pos[1]
            #north
            i = r-1
            while i >= 0:
                if matrix[i][c] == prev:
                    matrix[i][c] = curr
                i = i - 1
            #north east
            i = r - 1
            j = c + 1
            while i >= 0 and j < n:
                if matrix[i][j] == prev:
                    matrix[i][j] = curr
                i = i - 1
                j = j + 1
            #east
            j = c + 1
            while j < n:
                if matrix[r][j] == prev:
                    matrix[r][j] = curr
                j = j + 1
            #south east
            i = r + 1
            j = c + 1
            while i < n and j < n:
                if matrix[i][j] == prev:
                    matrix[i][j] = curr
                i = i + 1
                j = j + 1
            #south
            i = r + 1
            while i < n:
                if matrix[i][c] == prev:
                    matrix[i][c] = curr
                i = i + 1
            #south west
            i = r + 1
            j = c - 1
            while i < n and j >= 0:
                if matrix[i][j]  == prev:
                    matrix[i][j] = curr
                i = i + 1
                j = j - 1
            #west
            j = c - 1
            while j >= 0:
                if matrix[r][j] == prev:
                    matrix[r][j] = curr
                j = j - 1
            #north west
            i = r - 1
            j = c - 1
            while i >= 0 and j >= 0:
                if matrix[i][j] == prev:
                    matrix[i][j] = curr
                i = i - 1
                j = j - 1

            return matrix


        def dfs(matrix, rownum):
            j = 0
            while j < n:
                if matrix[rownum][j] == 0:
                    if rownum == n-1:
                        self.k = self.k + 1
                    else:
                        matrix[rownum][j] = 'Q'
                        blockCells([rownum,j],matrix,0,rownum+1)
                        dfs(matrix, rownum+1)
                        blockCells([rownum, j], matrix,rownum + 1,0)
                        matrix[rownum][j] = 0
                j = j + 1


        if n == 1:
            return 1

        i = 0
        self.k = 0
        r = 0
        while i < n:
            #create a n * n matrix
            matrix = [[0] * n for k in range(n)]

            #place Q in (0,i)
            matrix[0][i] = 'Q'

            #block cells based on Queen's position
            matrix = blockCells([0,i],matrix,0,1 )

            dfs(matrix, 1)

            r = r + self.k

            self.k = 0

            i = i + 1

        return r


o = Solution()
n = 4
print(o.totalNQueens(n))
