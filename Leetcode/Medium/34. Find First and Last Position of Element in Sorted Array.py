class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) == 0:
            return [-1, -1]

        left = -1
        right = -1

        # find left

        s = 0
        e = len(nums) - 1

        while s <= e:
            m = (s + e) // 2
            if nums[m] < target:
                s = m + 1
            elif nums[m] > target:
                e = m - 1
            else:
                if m == 0:
                    left = m
                    break
                elif nums[m - 1] != target:
                    left = m
                    break
                else:
                    e = m - 1
                    s = 0

        # find right

        s = 0
        e = len(nums) - 1

        while s <= e:
            m = (s + e) // 2
            if nums[m] < target:
                s = m + 1
            elif nums[m] > target:
                e = m - 1
            else:
                if m == len(nums) - 1:
                    right = m
                    break
                elif nums[m + 1] != target:
                    right = m
                    break
                else:
                    s = m + 1
                    e = len(nums) - 1

        return [left, right]


o =  Solution()
nums = [5,7,7,8,8,10]
target = 8
print(o.searchRange(nums,target))