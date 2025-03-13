class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """

        r = len(grid)
        c = len(grid[0])
        n = r * c

        NS = n*(n+1)/2
        NSS = n*(n+1)*(2*n + 1)/6

        RS = 0
        RSS = 0
        for i in range(r):
            for j in range(c):
                RS = RS + grid[i][j]
                RSS = RSS + grid[i][j] ** 2

        x = int((((RSS-NSS) / (RS-NS)) + (RS-NS)) / 2)
        y = int((((RSS-NSS) / (RS-NS)) - (RS-NS)) / 2)

        return [x,y]

o = Solution()
grid = [[9,1,7],[8,9,2],[3,4,6]]
print(o.findMissingAndRepeatedValues(grid))

