import math
class Solution:
    def maxAbsoluteSum(self, nums):
        smax = 0
        emax = 0

        smin = 0
        emin = 0

        maxsum = nums[0]
        minsum = nums[0]

        runsummax = 0
        runsummin = 0

        r = -1 * math.inf

        i = 0
        while i < len(nums):

            runsummax = runsummax + nums[i]
            runsummin = runsummin + nums[i]

            if runsummax > maxsum:
                maxsum = runsummax
            if runsummin < minsum:
                minsum = runsummin

            if runsummax < 0:
                smax = emax + 1
                if emax > len(nums) - 1:
                    return r
                emax = smax
                emin = emin + 1
                runsummax = 0
            elif runsummin > 0:
                smin = emin + 1
                if emin > len(nums) - 1:
                    return r
                emin = smin
                emax = emax + 1
                runsummin = 0
            else:
                emax = emax + 1
                emin = emin + 1

            i = i + 1

            r = max(r, abs(maxsum), abs(minsum))

        return r


o = Solution()
nums = [2,-5,1,-4,3,-2]
print(o.maxAbsoluteSum(nums))










