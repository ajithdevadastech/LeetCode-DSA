class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)

        if l == 1:
            return nums[0]

        if nums[0] < nums[l-1]:
            return nums[0]

        s = 0
        e = l-1

        while s <= e:
            mid = (s+e)//2
            if nums[mid] >= nums[0]:
                s = mid + 1
            else:
                if nums[mid - 1] < nums[mid]:
                    e = mid - 1
                else:
                    if mid < l-1:
                        if nums[mid] > nums[mid+1]:
                            s = mid + 1
                        else:
                            return nums[mid]
                    else:
                        return nums[mid]




o = Solution()
nums = [5,4,3,2,1]
print(o.findMin(nums))