class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        if m == 2:
            return position[-1] - position[0]

        def checkPositioning(mid):
            i = 0
            pos = position[0]
            k = m
            while i < len(position):
                if position[i] >= pos:
                    k = k - 1
                    pos = position[i] + mid
                i = i + 1

            if k <= 0:
                return True
            else:
                return False

        s = 0
        e = position[-1] - position[0]

        r = 0
        while s <= e:
            mid = (s + e) // 2
            possible = checkPositioning(mid)
            if possible:
                r = mid
                s = mid + 1
            else:
                e = mid - 1
        return r

o = Solution()
position = [79,74,57,22]
m = 4

# position = [1,2,3,4,7]
# m = 3
print(o.maxDistance(position, m))
