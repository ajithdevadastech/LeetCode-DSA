class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        self.memo = {}
        def helper(n):
            if n == 0:
                return 1
            elif n < 0:
                return 0
            elif n in self.memo.keys():
                return self.memo[n]
            else:
                self.memo[n] = helper(n-1) + helper(n-2)
                return self.memo[n]

        return helper(n)


o = Solution()
n = 3
print(o.climbStairs(n))
