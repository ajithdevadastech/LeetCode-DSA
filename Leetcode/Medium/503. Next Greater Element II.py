class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        """
        
        Algorithm:
        -------------
        
        1. 
        
        """

        if len(nums) == 1:
            return [-1]

        e = nums[0]
        flag = True
        x = 1
        while x < len(nums):
            if nums[x] != e:
                flag = False
            x = x + 1

        if flag:
            return [-1] * len(nums)

        stack = []
        dictstack = {}

        stack.append(0)
        i = 1
        loop = 0

        while loop < 2:
            while i < len(nums):
                while True:
                    if nums[stack[-1]] < nums[i]:
                        k = stack.pop()
                        dictstack[k] = nums[i]
                        if len(stack) == 0:
                            stack.append(i)
                            break
                        if stack[-1] == i:
                            dictstack[i] = -1
                            break
                        if nums[stack[-1]] > nums[i]:
                            stack.append(i)
                            break
                    else:
                        stack.append(i)
                        break
                i = i + 1
                if i == len(nums):
                    i = 0
                    loop = loop + 1
                    break

        if len(stack) > 0:
            for s in stack:
                if s not in dictstack.keys():
                    dictstack[s] = -1

        j = 0
        r = []
        while j < len(nums):
            r.append(dictstack[j])
            j = j + 1

        return r

o = Solution()
# nums = [1,2,1]
# nums = [1,2,3,4,5]
nums = [1,2,2]
print(o.nextGreaterElements(nums))
