class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 0:
            return 0

        #kadane's algorithm

        maxSum = nums[0]
        arrSum = 0

        s = 0
        e = 0

        while e < len(nums):
            arrSum = arrSum + nums[e]
            if arrSum < 0:
                s = e + 1
                if arrSum > maxSum:
                    maxSum = arrSum
                if s > len(nums) - 1:
                    break
                arrSum = 0
                e = s
            else:
                e = e + 1
                if arrSum > maxSum:
                    maxSum = arrSum

        return maxSum