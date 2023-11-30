class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        r = nums[0]

        i = 1
        while i < len(nums):
            r = r ^ nums[i]
            i = i + 1

        return r

o = Solution()

nums = [2,2,3,5,3]

print(o.singleNumber(nums))