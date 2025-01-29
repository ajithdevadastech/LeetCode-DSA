class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        nRows = len(grid)
        nCols = len(grid[0])

        self.grid = grid
        self.visited = []
        self.value = 0

        for i in range(nRows):
            self.visited.append(['c'] * nCols)

        def dfs(i,j):

            self.value = self.value + self.grid[i][j]
            self.visited[i][j] = 'v'
            #north
            n = i
            if n - 1 >= 0:
                if self.grid[n-1][j] > 0 and self.visited[n-1][j] == 'c':
                    #self.visited[n-1][j] = 'v'
                    dfs(n-1,j)
            #south

            s = i
            if s+1 <= nRows - 1:
                if self.grid[s+1][j] > 0 and self.visited[s+1][j] == 'c':
                    #self.visited[s+1][j] = 'v'
                    dfs(s+1,j)

            #east

            e = j
            if e + 1 <= nCols - 1:
                if self.grid[i][e+1] > 0 and self.visited[i][e+1] == 'c':
                    #self.visited[i][e+1] = 'v'
                    dfs(i, e+1)


            #west

            w = j
            if w-1 >= 0:
                if self.grid[i][w - 1] > 0 and self.visited[i][w - 1] == 'c':
                    #self.visited[i][w - 1] = 'v'
                    dfs(i, w-1)

        val = 0
        for i in range(nRows):
            for j in range(nCols):
                if self.visited[i][j] == 'c' and self.grid[i][j] != 0:
                    dfs(i,j)
                    if self.value > val:
                        val = self.value
                    self.value = 0

        return val

o = Solution()
grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
print(o.findMaxFish(grid))
