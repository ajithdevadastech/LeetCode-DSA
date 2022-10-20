class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        """
        sum [0,j] - sum[i,j] = sum[0, i-1]
        find all instances where sum[i,j] = k

        """

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            if nums[0] == k:
                return 1
            else:
                return 0

        r = 0

        d = {}
        d[0] = 1

        s = 0

        i = 0

        while i < len(nums):
            if nums[i] == k:
                r = r + 1
            else:
                s = s + nums[i]

                if (s - k) in d.keys():
                    r = r + 1

                if s in d.keys():
                    d[s] = d[s] + 1
                else:
                    d[s] = 1

            i = i + 1

        return r


o = Solution()
#nums = [1,1,1]
#k = 2
nums = [-1,-1, 1]
k = 0
print (o.subarraySum(nums, k))