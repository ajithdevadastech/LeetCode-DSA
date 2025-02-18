class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]

        r = []

        def helper(arr):
            if len(arr) == len(nums):
                arrcpy = arr.copy()
                r.append(arrcpy)
                return
            else:
                for i in nums:
                    if i not in arr:
                        arr.append(i)
                        helper(arr)
                        arr.pop()

        for n in nums:
            helper([n])
        return r

o = Solution()
nums = [1]
print(o.permute(nums))