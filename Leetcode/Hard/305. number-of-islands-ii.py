class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """

        """
        1. initialize m x n array
        2. for each item in positions, fill the array and calculate islands. store islands# in array. return r.
        3. calculate islands
        3.a. loop thru each element in array. If element is 1, increment island. Call helper by passing element.
        4. helper (array)
        4.a check for 1 in 4 directions, if yes recurse by sending the corresponding next element.
        4.b set element to 'V'
        
        """

        def CalculateIslands():
            for i in range(m):
                for j in range(n):
                    if self.mnarrcopy[i][j] == 1:
                        self.islandscount = self.islandscount + 1
                        helper(i,j)

        def helper(i, j):
            self.mnarrcopy[i][j] = 3
            if i < m-1:
                if self.mnarrcopy[i + 1][j] == 1:
                    helper(i+1,j)
            if i > 0 and self.mnarrcopy[i-1][j] != 3:
                if self.mnarrcopy[i - 1][j] == 1:
                    helper(i - 1, j)
            if j < n-1:
                if self.mnarrcopy[i][j+1] == 1:
                    helper(i, j+1)
            if j > 0 and self.mnarrcopy[i][j-1] != 3:
                if self.mnarrcopy[i][j - 1] == 1:
                    helper(i, j - 1)
            self.mnarrcopy[i][j] = 2
            return

        self.mnarr = []
        self.r = []
        self.islandscount = 0

        for i in range(m):
            self.mnarr.append([])

        for i in range(m):
            for j in range(n):
                self.mnarr[i].append(0)

        self.mnarrcopy = [[i for i in row] for row in self.mnarr]

        for pos in positions:
            self.mnarr[pos[0]][pos[1]] = 1
            self.mnarrcopy = [[i for i in row] for row in self.mnarr]
            self.islandscount = 0
            CalculateIslands()
            self.r.append(self.islandscount)

        return self.r


m = 3
n = 3
positions = [[0,0],[2,0],[0,1],[2,1],[0,2],[2,2],[0,1],[1,2]]

o = Solution()
print(o.numIslands2(m,n,positions))




