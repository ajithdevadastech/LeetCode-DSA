class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.pfnums = []

        i = 0
        for n in nums:
            self.pfnums.append(i + n)
            i = i + n

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.pfnums[right]
        else:
            return self.pfnums[right] - self.pfnums[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)