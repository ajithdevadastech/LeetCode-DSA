class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        """
        
        make a visited copy for board
        make a working copy for board
        go through the boundary, find 0s and dfs. Mark them as visited.
        loop through the matrix for unvisted nodes and set X on all 0s. return the board.
        

        """

        m = len(board)
        n = len(board[0])

        #make a visited copy for the board

        self.visited = []
        self.board = board


        for i in range(m):
            self.visited.append(['U']*n)

        def dfs(i,j):
            self.visited[i][j] = 'V'
            if i > 0:
                if self.board[i-1][j] == 'O' and self.visited[i-1][j] == 'U':
                    self.visited[i-1][j] = 'V'
                    dfs(i-1,j)
            if i < m-1:
                if self.board[i+1][j] == 'O' and self.visited[i+1][j] == 'U':
                    self.visited[i+1][j] = 'V'
                    dfs(i+1,j)
            if j > 0:
                if self.board[i][j-1] == 'O' and self.visited[i][j-1] == 'U':
                    self.visited[i][j-1] = 'V'
                    dfs(i,j-1)
            if j < n-1:
                if self.board[i][j+1] == 'O' and self.visited[i][j+1] == 'U':
                    self.visited[i][j+1] = 'V'
                    dfs(i,j+1)

        for a in range(n):
            if self.board[0][a] == 'O' and self.visited[0][a] == 'U':
                dfs(0,a)
        for b in range(m):
            if self.board[b][n-1] == 'O' and self.visited[b][n-1] == 'U':
                dfs(b,n-1)
        for c in range(n):
            if self.board[m-1][c] == 'O' and self.visited[m-1][c] == 'U':
                dfs(m-1,c)
        for d in range(m):
            if self.board[d][0] == 'O' and self.visited[d][0] == 'U':
                dfs(d,0)

        # update the board and return

        for i in range(m):
            for j in range(n):
                if self.visited[i][j] == 'U' and self.board[i][j] == 'O':
                    self.board[i][j] = 'X'

        return self.board

o = Solution()
board = [["O","X","O","O","O","X"],["O","O","X","X","X","O"],["X","X","X","X","X","O"],["O","O","O","O","X","X"],["X","X","O","O","X","O"],["O","O","X","X","X","X"]]
print(o.solve(board))





