class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def twoSumSmaller(subnums, subtarget):
            i = 0
            j = len(subnums) - 1
            count = 0
            while i < j:
                if subnums[i] + subnums[j] >= subtarget:
                    j = j - 1
                else:
                    count = count + j - i
                    i = i + 1
            return count


        nums = sorted(nums)
        k = 0
        r = 0
        while k < len(nums):
            r = r + twoSumSmaller(nums[k+1:], target + (-1 * nums[k]))
            k = k + 1

        return r

o = Solution()
nums = [3,1,0,-2]
target = 4
print(o.threeSumSmaller(nums, target))

