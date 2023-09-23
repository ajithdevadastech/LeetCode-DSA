class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 0 or len(nums) == 1:
            return nums

        # find left and right

        l = 0
        while True:
            if l > len(nums) - 1:
                break
            if nums[l] != 0:
                break
            else:
                l = l + 1

        r = len(nums) - 1
        while True:
            if r < 0:
                break
            if nums[r] != 2:
                break
            else:
                r = r - 1

        i = 0

        while i <= r:
            if nums[i] == 0:
                if l < i:
                    k = nums[i]
                    nums[i] = nums[l]
                    nums[l] = k
                    l = l + 1
                else:
                    i = i + 1
            elif nums[i] == 1:
                i = i + 1
            else:
                k = nums[i]
                nums[i] = nums[r]
                nums[r] = k
                r = r - 1

        return nums