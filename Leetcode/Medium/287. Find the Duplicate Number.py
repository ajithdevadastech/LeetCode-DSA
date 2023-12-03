class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        xor = nums[0]
        i = 1

        while i < len(nums):
            xor = xor ^ nums[i]
            if xor == p2:
                break
            i = i + 1

        return nums[i]

o = Solution()
nums = [3,1,3,4,2]
print(o.findDuplicate(nums))