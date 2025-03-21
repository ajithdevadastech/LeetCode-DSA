class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if len(nums) == 1 and k == 1:
            return nums[0]

        if k == 1:
            return min(nums)

        L = len(nums)

        self.minval = float('inf')

        def helper(i, val, n):
            if (k - n) > (L-1-i):
                return self.minval

            if n == k:
                if val < self.minval:
                    self.minval = val
                return self.minval

            x = 2
            while x + i <= L-1:
                helper(i+x, max(val, nums[x+i]), n+1)
                x = x + 1



        r = float('Inf')
        i = 0
        for n in nums:
            val = n
            helper(i, val, 1)
            if self.minval < r:
                r = self.minval
            self.minval = float('inf')
            i = i + 1

        return r

o = Solution()
nums = [2,7,9,3,1]
k = 2
print(o.minCapability(nums,k))
