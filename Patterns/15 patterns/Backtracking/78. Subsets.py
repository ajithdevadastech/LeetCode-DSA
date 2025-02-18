class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = [[]]

        if len(nums) == 1:
            ans.append(nums)
            return ans

        def helper(arr, ind):
            if ind < len(nums):
                arrcpy = arr.copy()
                ans.append(arrcpy)
                i = ind + 1
                while i < len(nums):
                    arr.append(nums[i])
                    helper(arr,i)
                    arr.pop()
                    i = i + 1
            else:
                return


        k = 0
        for n in nums:
            helper([n], k)
            k = k + 1

        return ans

o = Solution()
nums = [1,2,3]
print(o.subsets(nums))