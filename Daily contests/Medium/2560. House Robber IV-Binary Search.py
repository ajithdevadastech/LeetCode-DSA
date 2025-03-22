class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def helper(val):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= val:
                    count = count + 1
                    i = i + 2
                else:
                    i = i + 1
                if count >= k:
                    return True
            return False


        s = min(nums)
        e = max(nums)

        while s <= e:
            if s == e:
                return s
            if s == e - 1:
                if helper(s):
                    return s
                if helper(e):
                    return e
            mid = int((s+e)/2)
            if helper(mid):
                e = mid
            else:
                s = mid

o = Solution()
nums = [2,3,5,9,4]
k = 3
print(o.minCapability(nums,k))

        