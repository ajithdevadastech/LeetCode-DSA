class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        #use stack for nums2 and populate for nums1

        nums1Dict = {}
        i = 0
        r = []
        for n in nums1:
            nums1Dict[n] = i
            r.append(-1)
            i = i + 1

        stack = [nums2[0]]

        i = 1
        while i < len(nums2):
            if len(stack) == 0:
                stack.append(nums2[i])
            elif nums2[i] < stack[-1]:
                stack.append(nums2[i])
            else:
                while True:
                    if len(stack) == 0:
                        stack.append(nums2[i])
                        break
                    elif nums2[i] < stack[-1]:
                        stack.append(nums2[i])
                        break
                    else:
                        if stack[-1] in nums1Dict.keys():
                            r[nums1Dict[stack[-1]]] = nums2[i]
                        stack.pop()

            i = i + 1

        return r

o = Solution()
nums1 = [2,4]
nums2 = [1,2,3,4]
print(o.nextGreaterElement(nums1,nums2))







