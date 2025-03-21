
class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            if nums[0] == 0:
                return 0
            else:
                return 1


        #find the 1st positive index using binary search
        s = 0
        e = len(nums )- 1

        while s <= e:
            if e == s + 1:
                if nums[s] > 0:
                    pos = len(nums) - s
                else:
                    if e == len(nums) - 1:
                        if nums[e] > 0:
                            pos = 1
                        else:
                            pos = 0
                    else:
                        pos = len(nums) - e
                break
            if nums[int((s+e)/2)] > 0:
                e = int((s + e)/2)
            else:
                s = int((s+e)/2)

        # find the 1st negative index using binary search
        s = 0
        e = len(nums) - 1

        while s <= e:
            if e == s + 1:
                if nums[e] < 0:
                    neg = e+1
                else:
                    if s == 0:
                        if nums[s] < 0:
                            neg = 1
                        else:
                            neg = 0
                    else:
                        neg = s+1
                break
            if nums[int((s+e)/2)] < 0:
                s = int((s+e)/2)
            else:
                e = int((s + e) / 2)

        return max(pos, neg)

o = Solution()
nums = [0,0]
print(o.maximumCount(nums))
