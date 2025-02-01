class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        self.grid = grid

        nRows = len(self.grid)
        nCols = len(self.grid[0])

        self.dict = {}

        def dfs (i, j, iCount):
            self.grid[i][j] = iCount

            if iCount in self.dict.keys():
                self.dict[iCount] =  self.dict[iCount] + 1
            else:
                self.dict[iCount] = 1

            #north
            if i-1 >= 0:
                if self.grid[i-1][j] == 1:
                    self.grid[i-1][j] = iCount
                    dfs(i-1,j,iCount)
            #south
            if i+1 <= nRows-1:
                if self.grid[i+1][j] == 1:
                    self.grid[i+1][j] = iCount
                    dfs(i + 1, j, iCount)
            #west
            if j-1 >= 0:
                if self.grid[i][j-1] == 1:
                    self.grid[i][j-1] = iCount
                    dfs(i, j-1, iCount)
            #east
            if j+1 <= nCols-1:
                if self.grid[i][j+1] == 1:
                    self.grid[i][j+1] = iCount
                    dfs(i, j+1, iCount)

        oneCount = 0
        iCount =  2
        for r in range(nRows):
            for c in range(nCols):
                if self.grid[r][c] == 1:
                    dfs(r,c,iCount)
                    iCount = iCount + 1
                    oneCount = oneCount + 1

        if oneCount == 0:
            return 1


        #calculate island size by flipping each zeroes

        ret = 0
        for d in self.dict.values():
            if d > ret:
                ret = d

        for r in range(nRows):
            for c in range(nCols):
                neighbors = {}
                if self.grid[r][c] == 0:
                    #north
                    if r-1 >= 0:
                        if self.grid[r-1][c] != 0:
                            if self.grid[r-1][c] not in neighbors.keys():
                                neighbors[self.grid[r-1][c]] = 1
                    #south
                    if r+1 < nRows:
                        if self.grid[r+1][c] != 0:
                            if self.grid[r+1][c] not in neighbors.keys():
                                neighbors[self.grid[r+1][c]] = 1
                    #west
                    if c-1 >= 0:
                        if self.grid[r][c-1] != 0:
                            if self.grid[r][c-1] not in neighbors.keys():
                                neighbors[self.grid[r][c-1]] = 1
                    #east
                    if c+1 < nCols:
                        if self.grid[r][c+1] != 0:
                            if self.grid[r][c+1] not in neighbors.keys():
                                neighbors[self.grid[r][c+1]] = 1
                vSum = 0
                for n in neighbors.keys():
                    vSum = vSum + self.dict[n]
                if vSum > 0:
                    vSum = vSum + 1
                if vSum > ret:
                    ret = vSum

        return ret

o = Solution()
grid = [[0,0],[1,1]]
print(o.largestIsland(grid))










