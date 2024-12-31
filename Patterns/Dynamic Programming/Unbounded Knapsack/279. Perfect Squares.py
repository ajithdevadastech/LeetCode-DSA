import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        #create squares arr

        sqArr = []
        for i in range(1, int(math.sqrt(n))+1):
            sqArr.append(i**2)

        if n <= 3:
            sqArr = [1]

        self.dp = [float ('inf')] * (n+1)
        self.dp[0] = 0

        for i in range(1, n+1):
            for j in sqArr:
                if i == j:
                    self.dp[i] = 1
                elif i - j > 0:
                    if self.dp[i-j] + 1 < self.dp[i]:
                        self.dp[i] =  self.dp[i-j] + 1

        return self.dp[n]

o = Solution()
n = 12
print(o.numSquares(n))


