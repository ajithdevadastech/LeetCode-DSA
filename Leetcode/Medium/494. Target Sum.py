class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            if nums[0] * 1 == target or nums[0] * -1 == target:
                return 1
            else:
                return 0

        self.count = 0
        self.ht = {}


        def dfs(val, ci):
            if ci > len(nums) - 1:
                if target - val == 0:
                    return 1
                else:
                    return 0
            else:
                if (ci*20 + val) in self.ht.keys():
                    return self.ht[(ci*20 + val)]
                else:
                    self.ht[(ci*20 + val)] = dfs(val + nums[ci], ci + 1) + dfs(val - nums[ci], ci + 1)
                    return self.ht[(ci*20 + val)]

        return dfs(0,  0)


o = Solution()

nums = [9,7,0,3,9,8,6,5,7,6]
target = 2

print(o.findTargetSumWays(nums,target))

