class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #reference: https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d

        localMax = nums[0]
        globalMax = nums[0]

        for i in range(1, len(nums)):
            localMax = max(nums[i], localMax + nums[i])
            if localMax > globalMax:
                globalMax = localMax
        return globalMax

o = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(o.maxSubArray(nums))
