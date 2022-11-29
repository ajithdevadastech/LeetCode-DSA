class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        i = 1

        #initiate r

        r =  1
        for r1 in nums:
            r = r * r1

        c = nums[0]
        while i < len(nums):
            c = max(c * nums[i], nums[i])
            r = max(r, c)
            i = i + 1
        return r



o = Solution()
nums = [-2,3,-4]
print (o.maxProduct(nums))