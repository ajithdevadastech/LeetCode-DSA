class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        # make a visited copy for the board

        self.visited = []
        self.grid = grid
        self.count = 0

        for i in range(m):
            self.visited.append(['U'] * n)

        def dfs(i,j, mode):
            self.visited[i][j] = 'V'
            if mode == 'inside':
                self.count = self.count + 1
            if i > 0:
                if self.grid[i-1][j] == 1 and self.visited[i-1][j] == 'U':
                    dfs(i-1,j, mode)
            if i < m-1:
                if self.grid[i+1][j] == 1 and self.visited[i+1][j] == 'U':
                    dfs(i+1,j, mode)
            if j > 0:
                if self.grid[i][j-1] == 1 and self.visited[i][j-1] == 'U':
                    dfs(i,j-1, mode)
            if j < n-1:
                if self.grid[i][j+1] == 1 and self.visited[i][j+1] == 'U':
                    dfs(i,j+1, mode)

        #checking and dfs-ing the boundary cells
        mode = 'outside'
        for a in range(n):
            if self.grid[0][a] == 1 and self.visited[0][a] == 'U':
                dfs(0,a, mode)
        for b in range(m):
            if self.grid[b][n-1] == 1 and self.visited[b][n-1] == 'U':
                dfs(b,n-1,mode)
        for c in range(n):
            if self.grid[m-1][c] == 1 and self.visited[m-1][c] == 'U':
                dfs(m-1,c,mode)
        for d in range(m):
            if self.grid[d][0] == 1 and self.visited[d][0] == 'U':
                dfs(d,0, mode)

        # check the internal islands and count the 1s on each island

        mode = 'inside'
        for e in range(1, m-1):
            for f in range(1, n-1):
                if self.grid[e][f] == 1 and self.visited[e][f] == 'U':
                    dfs(e, f, mode)

        return self.count

o = Solution()
grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
print(o.numEnclaves(grid))





