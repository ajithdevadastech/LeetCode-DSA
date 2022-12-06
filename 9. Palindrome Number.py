class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        if x < 10:
            return True

        if x < 100:
            if x%10 == x//10:
                return True
            else:
                return False

        o = x
        n = 0


        k = 1

        while True:
            n = (o%10) + n*10
            otemp = o
            o = o//10
            if o <= n:
                if o < n:
                    n = n // 10
                    k = k /10
                break
            else:
                k = k * 10

        if o == n:
            if o == 0 and n == 0:
                return False
            if n < k:
                return False
            return True

        return False


o = Solution()
print(o.isPalindrome(112110))