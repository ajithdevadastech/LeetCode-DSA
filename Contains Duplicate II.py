class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        r = False

        d = {}

        i = 0

        while i < len(nums):
            if nums[i] in d.keys():
                r = True
            else:
                if len(d) >= k:
                    d.pop(list(d.keys())[0])
                d[nums[i]] = i

            i = i + 1

        return r


o = Solution()
nums = [1,2,3,1,2,3]
k = 2
print (o.containsNearbyDuplicate(nums, k))