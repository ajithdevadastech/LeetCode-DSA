class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        r = []

        # logic to build pattern

        N = int(n / 10)

        i = 1

        while i <= N:
            r.append(i)
            k = 0
            while k <= 9:
                if 10 * i + k > n:
                    break
                r.append(10 * i + k)
                k = k + 1
            i = i + 1

        # add remaining elements
        N = N + 1
        while N <= n:
            if N == 10:
                break
            r.append(N)
            N = N + 1

        return r


o = Solution()
n = 100
print(o.lexicalOrder(n))