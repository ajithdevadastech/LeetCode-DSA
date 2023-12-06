class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        1. n(n+1)/2 - sum
        2. xor from 0 to n XOR  xor all elements of array. The missing element won't cancel out.
        '''

        xorall = 0
        xorarr = nums[0]

        i = 1
        while i <= len(nums):
            xorall = xorall ^ i
            i = i + 1

        j = 1
        while j < len(nums):
            xorarr = xorarr ^ nums[j]
            j = j + 1

        return xorall ^ xorarr

o = Solution()
nums = [3,0,1]
print(o.missingNumber(nums))
