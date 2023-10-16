import math
class Solution (object):
    def minEatingSpeed(self, piles, h):

        s = 1
        e = max(piles)

        r = e

        j = 0
        while s <= e:
            m = (s+e)//2

            calch = 0
            i = 0
            while i < len(piles):
                calch = calch + int(math.ceil(piles[i]/m))
                i = i + 1
            if calch > h:
                s = m + 1
            elif calch < h:
                e = m - 1
                if j == 0:
                    r = m
                else:
                    if m < r:
                        r = m
            else:
                r = m
                e = m - 1
            j = j + 1

        return r

o = Solution()
piles = [1,1,1,999999999]
h = 10
print(o.minEatingSpeed(piles, h))