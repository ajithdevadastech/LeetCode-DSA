class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """

        ans = [0] * len(nums)
        if len(nums) == 1:
            return nums

        lesser = 0
        equal = 0
        greater = 0

        for num in nums:
            if num < pivot:
                lesser+=1
            elif num > pivot:
                greater+=1
            else:
                equal+=1

        li = 0
        ei = lesser
        gi = len(nums)- greater

        for num in nums:
            if num < pivot:
                ans[li] = num
                li = li + 1
            elif num == pivot:
                ans[ei] = num
                ei = ei + 1
            else:
                ans[gi] = num
                gi = gi + 1


        return ans

o = Solution()
nums = [9,12,5,10,14,3,10]
pivot = 10
print(o.pivotArray(nums,pivot))
