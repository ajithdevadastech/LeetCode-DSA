class Solution(object):

    def longestMonotonicSubarray(self, nums):

        L = len(nums)
        if L == 0:
            return 0
        if L == 1:
            return 1


        l = 1
        i = 0
        maxvalless = 1

        while i+1 < L:
            if nums[i] < nums[i+1]:
                l = l + 1
                if l > maxvalless:
                    maxvalless = l
            else:
                l = 1

            i = i + 1

        l = 1
        i = 0
        maxvalgreat = 1

        while i + 1 < L:
            if nums[i] > nums[i + 1]:
                l = l + 1
                if l > maxvalgreat:
                    maxvalgreat = l
            else:
                l = 1

            i = i + 1

        if maxvalless <= maxvalgreat:
            return maxvalgreat
        else:
            return maxvalless

o = Solution()
nums = [1,2]
print(o.longestMonotonicSubarray(nums))
