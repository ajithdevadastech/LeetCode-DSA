class Solution(object):

    def maxAscendingSum(self, nums):

        if len(nums) == 1:
            return nums[0]

        self.r = nums[0]

        i = 0
        s = nums[0]
        while i+1 < len(nums):
            if nums[i] < nums[i+1]:
                s = s + nums[i+1]
                if s > self.r:
                    self.r = s
            else:
                s = nums[i+1]
            i = i + 1

        return self.r

o = Solution()
nums = [12,17,15,13,10,11,12]
print(o.maxAscendingSum(nums))