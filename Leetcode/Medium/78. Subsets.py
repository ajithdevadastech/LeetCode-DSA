class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.ans = []

        def frecur(index, combination):
            self.ans.append([i for i in combination])
            index = index + 1
            if index > len(nums)-1:
                return
            else:
                m = index
                combr = [i for i in combination]
                while m < len(nums):
                    combr.append(nums[m])
                    frecur(m, combr)
                    m = m + 1
                    combr.pop()


        #driver
        self.ans.append([])
        i = 0
        while i < len(nums):
            frecur(i, [nums[i]])
            i = i + 1
        return self.ans

o = Solution()

nums = [1,2,3]
nums = [0]

print(o.subsets(nums))
