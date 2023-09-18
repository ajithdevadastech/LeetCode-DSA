class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        me = nums[0]

        i = 1
        c = 1
        while i < len(nums):
            if c == 0:
                me = nums[i]
            if nums[i] == me:
                c = c + 1
            else:
                c = c - 1
            i = i + 1

        return me

o = Solution()
nums = [6,5,5]
print(o.majorityElement(nums))

