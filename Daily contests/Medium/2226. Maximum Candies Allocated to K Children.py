class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """


        def checkifK(v):
            if v == 0:
                return False
            s = 0
            for c in candies:
                s = s + int(c/v)
            if s >= k:
                return True
            else:
                return False


        s = 0
        e = max(candies)

        while s <= e:
            if s == e:
                return s
            if s == e-1:
                if checkifK(e):
                    return e
                if checkifK(s):
                    return s
            m = int((s+e)/2)
            if checkifK(m):
                s = m
            else:
                e = m

        return 0

o = Solution()
candies = [9,10,1,2,10,9,9,10,2,2]
k = 3
print(o.maximumCandies(candies,k))

