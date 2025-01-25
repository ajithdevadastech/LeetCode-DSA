class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """

        """
        1. put 1s beside all 0s
        2. Loop through blank cells
        3. find minimum val after calculating all valid values
        4 return matrix
        """

        #initialize matrix

        nRows = len(isWater)
        nCols = len(isWater[0])

        self.matrix = []
        for i in range(nRows):
            k = [nRows+nCols] * nCols
            self.matrix.append(k)

        def bfs(i,j,val):
            #north
            if i-1 >= 0:
                val = self.matrix[i][j] + 1
                if val < self.matrix[i-1][j]:
                    self.matrix[i-1][j] = val
                    bfs(i-1,j,val)
                # else:
                #     return
            #south
            if i+1 <= nRows - 1:
                val = self.matrix[i][j] + 1
                if val < self.matrix[i+1][j]:
                    self.matrix[i+1][j] = val
                    bfs(i+1,j,val)
                # else:
                #     return
            #east

            if j+1 <= nCols - 1:
                val = self.matrix[i][j] + 1
                if val < self.matrix[i][j+1]:
                    self.matrix[i][j+1] = val
                    bfs(i,j+1,val)
                # else:
                #     return

            #west

            if j-1 >= 0:
                val = self.matrix[i][j] + 1
                if val < self.matrix[i][j-1]:
                    self.matrix[i][j-1] = val
                    bfs(i,j-1,val)
                # else:
                #     return

        #set water cells to 0
        for i in range(nRows):
            for j in range(nCols):
                if isWater[i][j] == 1:
                    self.matrix[i][j] = 0
                    bfs(i,j,0)

        return self.matrix


o = Solution()
isWater = isWater = [[0,0,1],[1,0,0],[0,0,0]]
print(o.highestPeak(isWater))













