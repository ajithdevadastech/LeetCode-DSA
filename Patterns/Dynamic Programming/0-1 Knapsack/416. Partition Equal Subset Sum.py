"""
class Solution(object):
    def canPartition(self, nums):

        :type nums: List[int]
        :rtype: bool

        if sum(nums) % 2 > 0:
            return False

        midval = int(sum(nums)/2)
        self.memo = {}

        # 0/1 knapsack algorithm
        def helper(val, arr):
            if val == 0:
                return True
            elif val < 0 or len(arr) == 0:
                return False
            else:
                if tuple([val, tuple(arr)]) in self.memo.keys():
                    return self.memo[tuple([val, tuple(arr)])]
                else:
                    self.memo[tuple([val, tuple(arr)])] = helper(val - arr[-1], arr[:-1]) or helper(val, arr[:-1])
                    return self.memo[tuple([val, tuple(arr)])]

        return helper(midval, nums)
"""



#bottom up approach
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 > 0:
            return False
        midval = int(sum(nums) / 2)

        #create 2d dp array [nums+1][midval+1]

        self.dp = []
        for i in range(len(nums)+1):
            arr = []
            for j in range(midval+1):
                arr.append('')
            self.dp.append(arr)

        #populate the base cases

        for j in range(1,midval+1):
            self.dp[len(nums)][j] = False

        for i in range(len(nums) + 1):
            self.dp[i][0] = True

        rows = len(nums) - 1
        cols = midval

        i = rows
        while i >= 0:
            j = 1
            while j <= midval:
                if j - nums[i] < 0:
                    self.dp[i][j] = self.dp[i + 1][j]
                else:
                    self.dp[i][j] = self.dp[i+1][j-nums[i]] or self.dp[i+1][j]
                j = j + 1
            i = i - 1

        return self.dp[0][midval]


o = Solution()
nums = [100,4,6]
print(o.canPartition(nums))
