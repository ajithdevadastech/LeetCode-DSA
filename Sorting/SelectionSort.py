
#https://leetcode.com/explore/learn/card/sorting/694/comparison-based-sorts/4434/
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i = 0
        l = len(nums) - 1

        while i <= l:
            m = min(nums[i:])
            ind = nums.index(m, i)
            if nums[i] > m:
                t = nums[i]
                nums[i] = m
                nums[ind] = t
            i = i + 1

        return nums

o = Solution()
nums = [2,0,4,3,5,3]
print(o.sortColors(nums))