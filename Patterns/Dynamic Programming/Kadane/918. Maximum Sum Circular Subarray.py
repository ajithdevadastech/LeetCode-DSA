class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        1. find maximum sum subarray and min sum subarray
        2. find total - maxsum and total - minsum
        3. the result will be max(maxsum, total-minsum)
        """

        self.localmin = nums[0]
        self.globalmin = nums[0]
        self.localmax = nums[0]
        self.globalmax = nums[0]

        total = sum(nums)
        def maxminsubarray(nums):
            for i in range(1, len(nums)):
                self.localmax = max(nums[i], nums[i] + self.localmax)
                if self.localmax > self.globalmax:
                    self.globalmax = self.localmax

                self.localmin = min(nums[i], nums[i] + self.localmin)
                if self.localmin < self.globalmin:
                    self.globalmin = self.localmin

        maxminsubarray(nums)
        if total == self.globalmin:
            return self.globalmax
        else:
            return max(self.globalmax, total - self.globalmin)

o = Solution()
nums = [-3,-2,-3]
print(o.maxSubarraySumCircular(nums))

