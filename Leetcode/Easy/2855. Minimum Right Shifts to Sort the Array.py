class Solution(object):
    def minimumRightShifts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            return 0

        i = 0
        r = 0
        flag = False
        max = nums[0]

        while i <= len(nums) - 2:
            if nums[i+1] > nums[i]:
                if flag is False:
                    if i == len(nums) - 2:
                        return 0
                else:
                    if nums[i+1] > max:
                        return -1
                    else:
                        r = r + 1
            else:
                if flag is False:
                    flag = True
                    r = r + 1
                    #max = nums[i]
                else:
                    return -1
            i = i + 1

        return r

o = Solution()
nums = [3,4,5,1,2]
#nums = [3,2]
#nums = [29, 30, 88, 28, 62]
nums = [2,1,4]
print(o.minimumRightShifts(nums))