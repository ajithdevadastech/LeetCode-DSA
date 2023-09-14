class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        s = 0
        e = len(nums) - 1

        if target < nums[s]:
            return 0
        if target > nums[e]:
            return len(nums)



        while e >= s:
            i = (s + e) // 2
            if nums[i] == target:
                return i
            elif target < nums[i]:
                if target > nums[i - 1]:
                    return i
                else:
                    e = i - 1
            elif target > nums[i]:
                if target < nums[i + 1]:
                    return i+1
                else:
                    s = i + 1