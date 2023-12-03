class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        i = 0
        arr = []
        while i <= n:
            j = 0
            count = 0
            while j <= 32:
                if i & (1 << j) > 0:
                    count = count + 1
                j = j + 1
            arr.append(count)
            i = i + 1
        return arr

o = Solution()
print(o.countBits(5))