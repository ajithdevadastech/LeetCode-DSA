class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        i = 0
        while i+1 <= len(nums) - 1:
            if nums[i] ==nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
                i = i + 2
            else:
                i = i + 1

        #shift all 0s

        r = [0] * len(nums)
        i = 0
        for n in nums:
            if n > 0:
                r[i] = n
                i = i + 1
        return r

nums = [1,2,2,1,1,0]
o = Solution()
print(o.applyOperations(nums))

