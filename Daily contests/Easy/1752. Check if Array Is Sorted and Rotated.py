class Solution():
    def check(self, nums):

        #checks
        L = len(nums)
        if L == 0:
            return False
        if L == 1 or L == 2:
            return True

        if nums[0] < nums[L-1]:
            #linear search, return False if decreased once
            i = 0
            while i+1 < L:
                if nums[i] > nums[i+1]:
                    return False
                else:
                    i = i + 1
        else:
            #linear search until first dip and then again linear search, return False if decreased more than once
            i = 0
            w = 0
            while i+1 < L:
                if nums[i] > nums[i+1]:
                    w = w + 1
                    if w > 1:
                        return False
                i = i + 1

        return True

o = Solution()
nums = [6,10,6]
print(o.check(nums))