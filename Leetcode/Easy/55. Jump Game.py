class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        i = 0
        max_reachable = 0

        while True:
            if max_reachable < i + nums[i]:
                max_reachable = i + nums[i]
            if i + nums[i] >= len(nums) - 1:
                return True
            else:
                i = i + 1
            if i > max_reachable:
                break
        return False

o = Solution()
nums = [2,3,1,1,4]
print(o.canJump(nums))

