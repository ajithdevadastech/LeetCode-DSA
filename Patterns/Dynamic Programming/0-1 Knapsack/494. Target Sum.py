class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target > sum(nums) or target < -1 * sum(nums):
            return 0
        n = 2 * sum(nums) + 1

        #initialize curr and next arr

        self.curr = []
        for i in range(n):
            self.curr.append(0)

        self.next = self.curr[:]

        #set first index values on curr

        self.curr[sum(nums) - nums[0]] += 1
        self.curr[sum(nums) + nums[0]] += 1

        for i in range(1,len(nums)):
            k = 0
            for j in range(2*sum(nums) + 1):
                if self.curr[j] > 0:
                    self.next[j-nums[i]] = self.next[j-nums[i]] + self.curr[j]
                    self.next[j+nums[i]] = self.next[j+nums[i]] + self.curr[j]
            self.curr = self.next[:]
            self.next = [0] * n

        return self.curr[sum(nums)+target]


o = Solution()
nums = [1,0]
target = 1
print(o.findTargetSumWays(nums, target))