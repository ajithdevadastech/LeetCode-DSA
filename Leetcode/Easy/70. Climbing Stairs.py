class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ht = {}

        def f(i, n):
            if i > n:
                return 0
            elif i == n:
                return 1
            elif i < n:
                if i in self.ht.keys():
                    return self.ht[i]
                else:
                    self.ht[i] = f(i+1, n) + f(i+2, n)
                    return self.ht[i]


        return f(0, n)

o = Solution()
n = 10
print(o.climbStairs(n))
