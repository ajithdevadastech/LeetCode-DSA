import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # creating frequency hash map
        d = {}
        for n in nums:
            if n in d.keys():
                d[n] = d[n] + 1
            else:
                d[n] = 1

        d1 = {}
        for key, val in d.items():
            d1[val] = key


        # heap operation k - sized heap

        #create heap for the first k elements
        h = []
        for d in d1.keys():
            h.append(d)

        heapq.heapify(h[0:k])

        i = k
        while i < len(nums):
            #push and then pop
            heapq.heappushpop(h, nums[i])
            i = i + 1

        arr = heapq.nlargest(k, h)
        r = []
        for a in arr:
            r.append(d1[a])
        return r


o = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(o.topKFrequent(nums,k))


