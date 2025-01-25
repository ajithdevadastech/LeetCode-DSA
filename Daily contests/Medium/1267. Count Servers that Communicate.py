class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nRows = len(grid)
        nCols = len(grid[0])

        self.grid = grid
        self.val = 0

        def dfs (i,j):

            self.grid[i][j] = -1
            #look for 1 in all directions and do dfs
            #north
            n = i
            while n-1 >= 0:
                if self.grid[n-1][j] == 1:
                    self.val = self.val + 1
                    dfs(n-1,j)
                n = n - 1
            #south
            s = i
            while s+1 <= nRows - 1:
                if self.grid[s+1][j] == 1:
                    self.val = self.val + 1
                    dfs(s+1,j)
                s = s + 1
            #east
            e = j
            while e+1 <= nCols - 1:
                if self.grid[i][e+1] == 1:
                    self.val = self.val + 1
                    dfs(i,e+1)
                e = e + 1
            #west
            w = j
            while w - 1 >= 0:
                if self.grid[i][w-1] == 1:
                    self.val = self.val + 1
                    dfs(i, w-1)
                w = w - 1

        r = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == 1:
                    dfs(i,j)
                    if self.val > 0:
                        self.val = self.val + 1
                    r = r + self.val
                    self.val = 0

        return r


o = Solution()
grid = [[1,0],[1,1]]
print(o.countServers(grid))
