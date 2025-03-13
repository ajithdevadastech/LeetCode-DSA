class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        #https://www.youtube.com/watch?v=99ExTh_0Ycg

        if n == 1:
            return True

        # find k : 3**k < n

        k = 0
        s = 0
        while s < n:
            s = s + 3 ** k
            k = k + 1

        k = k - 1

        r = n - 3 ** k

        i = k - 1
        while i >= 0:
            if r >= 3 ** i:
                r = r - 3 ** i
            if  r == 0:
                return True
            else:
                i = i - 1
        return False



o = Solution()
n = 92
print(o.checkPowersOfThree(n))
