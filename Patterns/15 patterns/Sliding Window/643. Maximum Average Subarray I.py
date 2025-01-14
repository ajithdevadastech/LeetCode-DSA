class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        #navigate until kth value

        i = 0
        sval = 0
        while i < k:
            sval = sval+nums[i]
            i = i + 1

        maxval = sval
        #sliding window
        i = 0
        j = k-1
        while j < len(nums)-1:
            sval = sval - nums[i] + nums[j+1]
            i = i + 1
            j = j + 1
            if sval > maxval:
                maxval = sval

        return maxval/k

o = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(o.findMaxAverage(nums,k))





