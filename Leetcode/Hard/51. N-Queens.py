class Solution(object):
    def solveNQueens(self, n):

        if n == 1:
            return [['Q']]

        self.ans = []
        board = [['.'] * n for m in range(n)]

        def isSafe(r,c):

            #north west check
            i = r
            j = c

            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i = i - 1
                j = j - 1

            #north check

            i = r
            j = c
            while i >= 0:
                if board[i][j] == 'Q':
                    return False
                i = i - 1

            #north east check

            i = r
            j = c

            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i = i - 1
                j = j + 1

            return True

        def ansformat(matr):
            r = []
            k = 0
            while k < n:
                l = 0
                s = ""
                while l < n:
                    s = s + board[k][l]
                    l = l + 1
                r.append(s)
                k = k + 1
            return r

        def frecur(row):
            if row == n:
                return
            elif row == n-1:
                c = 0
                while c < n:
                    if isSafe(row,c):
                        board[row][c] = 'Q'
                        self.ans.append(ansformat(board))
                        board[row][c] = '.'
                    c = c + 1
                return
            else:
                c = 0
                while c < n:
                    if isSafe(row, c):
                        board[row][c] = 'Q'
                        frecur(row+1)
                        board[row][c] = '.'
                    c = c + 1

        #driver
        c = 0
        while c < n:
            board[0][c] = 'Q'
            frecur(1)
            board[0][c] = '.'
            c = c + 1

        return self.ans


o = Solution()
n = 5
print(o.solveNQueens(n))



