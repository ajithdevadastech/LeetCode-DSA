class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        1. find localmax and localmin at each point to handle -ve * -ve scenario
        2. kadane's
        """

        localmax = nums[0]
        localmin = nums[0]
        globalmax = nums[0]

        for i in range(1, len(nums)):
            lmax = max(nums[i], localmax * nums[i], localmin * nums[i])
            lmin = min(nums[i], localmax * nums[i], localmin * nums[i])
            if lmax > globalmax:
                globalmax = lmax
            localmax = lmax
            localmin = lmin
        return globalmax

o = Solution()
nums = [-4, -3, -2]
print(o.maxProduct(nums))