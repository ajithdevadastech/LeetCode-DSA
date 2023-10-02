from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if len(nums) == 1 and k == 1:
            return nums[0]

        ans = []

        indexArr = []
        dq = deque(indexArr)

        #process first k elements

        i = 0
        while i < k:
            #remove lower valued indices and keep only higher valued index in dq right
            while True:
                if len(dq) == 0:
                    dq.append(i)
                    break
                elif nums[dq[-1]] <= nums[i]:
                    dq.pop()
                else:
                    dq.append(i)
                    break
            i = i+1

        ans.append(nums[dq[0]])

        #after k elements

        while i < len(nums):
            #remove unwanted indices from dq left
            while len(dq) > 0:
                if dq[0] < i-k+1:
                    dq.popleft()
                else:
                    break
            # remove lower valued indices and keep only higher valued index in dq right
            while True:
                if len(dq) == 0:
                    dq.append(i)
                    break
                elif nums[dq[-1]] <= nums[i]:
                    dq.pop()
                else:
                    dq.append(i)
                    break
            ans.append(nums[dq[0]])
            i = i + 1

        return ans

o = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(o.maxSlidingWindow(nums,k))





