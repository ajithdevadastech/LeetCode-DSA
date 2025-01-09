class Solution(object):
    def maximumSumScore(self, nums):

        if len(nums) == 1:
            return nums[0]

        #find prefix sum array forward

        farr = [nums[0]]
        index = 0
        for i in range(1, len(nums)):
            farr.append(farr[index] + nums[i])
            index = index + 1

        #find prefix sum backward
        barr = [nums[len(nums) - 1]]
        j = len(nums) - 2
        while j >= 0:
            barr.insert(0,barr[0] + nums[j])
            j = j - 1

        val = float('-inf')

        k = 0
        while k <= len(nums) - 1:
            if max(farr[k], barr[k]) > val:
                val = max(farr[k], barr[k])
            k = k + 1

        return val

o = Solution()
nums = [-1,-4,2,3,4]
print(o.maximumSumScore(nums))

