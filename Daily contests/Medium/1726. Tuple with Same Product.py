import math


class Solution(object):
    def tupleSameProduct(self, nums):

        if len(nums) < 4:
            return 0

        dict = {}

        r = 0

        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] * nums[j] not in dict.keys():
                    dict[nums[i] * nums[j]] = 1
                else:
                    #r = r + 8 * dict[nums[i] * nums[j]]
                    dict[nums[i] * nums[j]] = dict[nums[i] * nums[j]] + 1
                j = j + 1
            i = i + 1

        for d in dict.keys():
            if dict[d] > 1:
                r = r + 8 * math.factorial(dict[d])/2 * math.factorial(dict[d]-2)
        return int(r)

o = Solution()
nums = [1,2,4,5,10]
print(o.tupleSameProduct(nums))
