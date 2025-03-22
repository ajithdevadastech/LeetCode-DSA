class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """

        s = 1
        e = max(ranks) * (cars**2)

        def helper(time):
            val = 0
            for r in ranks:
                val = val + int((time/r)**0.5)
            if val >= cars:
                return True
            else:
                return False

        while s <= e:
            if s == e:
                return s
            if s == e-1:
                if helper(s):
                    return s
                if helper(e):
                    return e

            mid = int((s+e)/2)
            if helper(mid):
                e = mid
            else:
                s = mid

o = Solution()
ranks = [1]
cars = 1
print(o.repairCars(ranks,cars))



