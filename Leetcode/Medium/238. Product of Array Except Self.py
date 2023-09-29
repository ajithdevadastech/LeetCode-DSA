class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # precalculate right array

        r = [1]
        pr = 1
        i = len(nums) - 2
        while i >= 0:
            pr = pr * nums[i + 1]
            r.append(pr)
            i = i - 1

        r = r[::-1]
        # change r while navigating left

        pl = 1
        j = 1
        while j < len(nums):
            pl = pl * nums[j - 1]
            r[j] = r[j] * pl
            j = j + 1

        return r

o = Solution()
nums = [1,2,3,4]
print(o.productExceptSelf(nums))