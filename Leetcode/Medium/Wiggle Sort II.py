class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        L = len(nums)
        i = 0

        while i < L:
            if i % 2 == 0:
                if i < L-1:
                    if nums[i + 1] > nums[i]:
                        i = i + 1
                    elif nums[i + 1] < nums[i]:
                        # swap
                        t = nums[i]
                        nums[i] = nums[i + 1]
                        nums[i + 1] = t
                        i = i + 1
                    else:
                        j = i + 2
                        while True:
                            if j == L:
                                i = j
                                break
                            if nums[j] > nums[i]:
                                t = nums[i+1]
                                nums[i+1] = nums[j]
                                nums[j] = t
                                i = i + 1
                                break
                            elif nums[j] < nums[i]:
                                t = nums[i]
                                nums[i] = nums[j]
                                nums[j] = t
                                i = i + 1
                                break
                            else:
                                j = j + 1
                else:
                    break
            else:
                if i < L-1:
                    if nums[i + 1] < nums[i]:
                        i = i + 1
                    elif nums[i + 1] > nums[i]:
                        # swap
                        t = nums[i]
                        nums[i] = nums[i + 1]
                        nums[i + 1] = t
                        i = i + 1
                    else:
                        j = i + 2
                        while True:
                            if j == L:
                                i = j
                                break
                            if nums[j] < nums[i]:
                                t = nums[i+1]
                                nums[i+1] = nums[j]
                                nums[j] = t
                                i = i + 1
                                break
                            elif nums[j] > nums[i]:
                                t = nums[i]
                                nums[i] = nums[j]
                                nums[j] = t
                                i = i + 1
                                break
                            else:
                                j = j + 1
                else:
                    break

        return nums


o = Solution()
nums = [1,4,3,4,1,2,1,3,1,3,2,3,3]
print(o.wiggleSort(nums))

# loop through arr
# if index is even:
#     check if next value is greater, if yes index++, next
#     elif check if next value is lesser, if yes swap curr and next. index ++ , next
#     else loop until a different value is found (if not found exit). if a greater value is found, swap with next element. if a lesser value is found, sawp with curr element. index++, next
# if index is odd:
#     ndex is even:
#     check if next value is lesser, if yes index++, next
#     elif check if next value is greater, if yes swap curr and next. index ++ , next
#     else loop until a different value is found (if not found exit). if a lesser value is found, swap with next element. if a greater value is found, swap with curr element. index++, next



