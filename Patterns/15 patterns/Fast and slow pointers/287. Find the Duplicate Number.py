class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        slow = nums[0]
        fast = nums[0]

        # find the meeting point

        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break

        mp = slow

        # find duplicate - where the loop starts

        L = nums[0]
        R = slow

        while L != R:
            L = nums[L]
            R = nums[R]

        return L


o = Solution()
nums = [4,3,1,4,2]
print(o.findDuplicate(nums))