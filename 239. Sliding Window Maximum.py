from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if k == 1:
            return nums
        if len(nums) == 0:
            return nums


        r = []
        d = deque()
        d.append(nums[0])

        #process first k elements

        i = 1
        while i < k:
            while True:
                if len(d) > 0:
                    if d[-1] <= nums[i]:
                        d.pop()
                    else:
                        d.append(nums[i])
                        break
                else:
                    d.append(nums[i])
                    
                if i == k-1:
                    break

            i = i + 1

        r.append(d[0])

        #loop through the remaining elements

        while i < len(nums):
            if len(d) == k:
                d.popleft()
            while True:
                if len(d) > 0:
                    if d[-1] <= nums[i]:
                        d.pop()
                    else:
                        break
                else:
                    d.append(nums[i])
                    break
            r.append(d[0])
            i = i + 1

        return r

o = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(o.maxSlidingWindow(nums,k))





