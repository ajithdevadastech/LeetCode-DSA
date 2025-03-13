class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1

        if n == 2:
            return 5

        k = 1
        i = 3
        r = 5
        while i <= n:
            r = r + 4 + k * 4
            k = k + 1
            i = i + 1

        return r


o = Solution()
n = 5
print(o.coloredCells(n))
