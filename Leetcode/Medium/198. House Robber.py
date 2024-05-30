class Solution(object):
    #maxval = 0
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        dictM = {}

        def helper(n,s):
            if n > len(nums) - 1:
                return 0
            elif n in dictM.keys():
                return dictM[n]
            else:
                s = max(helper(n+1, s), nums[n] + helper(n+2, s))
                dictM[n] = s
                return s


        return helper(0,0)


o = Solution()
#nums = [1, 2, 3, 1]
#nums = [2,7,9,3,1]
#nums = [1,2,1,1]
#nums = [4,1,2,7,5,3,1]
print(o.rob(nums))
