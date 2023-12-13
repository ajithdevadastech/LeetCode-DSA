import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        arr = nums[0:k]
        heapq.heapify(arr)

        i = k
        while i < len(nums):
            heapq.heappush(arr,nums[i])
            heapq.heappop(arr)
            i = i+1

        return heapq.heappop(arr)

o = Solution()
nums = [-3, -2, 4, 0, 4]
k = 1
print(o.findKthLargest(nums,k))

