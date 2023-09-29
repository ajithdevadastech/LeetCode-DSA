class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        ans = 0

        i = 0
        pr = 1
        while i < len(nums):
            if nums[i] == 0:
                pr = 1
            else:
                pr = pr * nums[i]
                ans = max(ans, pr)
            i = i + 1

        j = len(nums) - 1
        pl = 1
        while j>=0:
            if nums[j] == 0:
                pl = 1
            else:
                pl = pl * nums[j]
                ans = max(ans, pl)
            j = j - 1

        return ans