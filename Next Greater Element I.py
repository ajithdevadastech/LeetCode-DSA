class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        stack = []
        dictNext = {}

        r = []

        while len(nums2) > 0:
            k = nums2.pop(0)
            if len(stack) == 0:
                stack.append(k)
            else:
                while True:
                    if len(stack) == 0:
                        break
                    if k > stack[-1]:
                        dictNext[stack[-1]] = k
                        stack.pop()
                    else:
                        break
                stack.append(k)

        for i in stack:
            dictNext[i] = -1

        for j in nums1:
            r.append(dictNext[j])

        return r


o =  Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(o.nextGreaterElement(nums1, nums2))