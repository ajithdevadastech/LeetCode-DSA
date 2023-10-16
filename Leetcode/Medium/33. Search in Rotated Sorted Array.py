class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # if midpoint is rotated part:
        #     if target < midpoint:
        #         if target > end:
        #             search left
        #         if target < end:
        #             search right
        #     if target > midpoint:
        #         search right

        # if midpoint is not in rotated part:
        #     if target < midpoint:
        #         search left
        #     if target > midpoint:
        #         if target < start:
        #             search right
        #         if target > start:
        #             search left

        index = - 1

        s = 0
        e = len(nums) - 1

        #binary search for non rotated

        indexb = -1
        if nums[s] < nums[e]:
            while s <= e:
                m = (s + e) // 2
                if target < nums[m]:
                    e = m - 1
                elif target > nums[m]:
                    s = m + 1
                else:
                    return m
            return indexb
        else:
            s = 0
            e = len(nums) - 1
            while s <= e:
                m = (s+e)//2
                if nums[m] == target:
                    index = m
                    break
                #midpoint in rotated part
                if nums[m] > nums[len(nums) - 1]:
                    if target < nums[m]:
                        if target > nums[len(nums) - 1]:
                            e = m - 1
                        else:
                            s = m + 1
                    else:
                        s = m + 1
                else:
                    if target < nums[m]:
                        e = m - 1
                    elif target > nums[m]:
                        if target < nums[0]:
                            s = m + 1
                        else:
                            e = m - 1
            return index

o = Solution()
nums = [3,1]
target = 1
print(o.search(nums,target))
