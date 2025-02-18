import heapq
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        minval = 0
        heapq.heapify(nums)

        while True:
            if len(nums) >= 2:
                v1 = heapq.heappop(nums)
                if v1 >= k:
                    return minval
                v2 = heapq.heappop(nums)
                # if v2 >= k:
                #     return minval
                heapq.heappush(nums, min(v1,v2)*2 + max(v1,v2))
                minval = minval + 1
            else:
                return minval


o = Solution()
nums = [999999999,999999999,999999999]
k = 1000000000

print(o.minOperations(nums,k))


