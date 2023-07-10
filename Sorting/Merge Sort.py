


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def mergeSortedArrays(arr1, arr2):

            l1 = len(arr1)
            l2 = len(arr2)

            i1 = 0
            i2 = 0

            r = []

            while True:
                if i1 < l1 and i2 < l2:
                    if arr1[i1] <= arr2[i2]:
                        r.append(arr1[i1])
                        i1 = i1 + 1
                    else:
                        r.append(arr2[i2])
                        i2 = i2 + 1
                if i1 == l1:
                    r.extend(arr2[i2:])
                    break
                if i2 == l2:
                    r.extend(arr1[i1:])
                    break

            return r

        def mergeSort(arr):
            l = len(arr)
            if l == 1:
                return [arr[0]]
            if l == 2:
                if arr[0] <= arr[1]:
                    return [arr[0], arr[1]]
                else:
                    return [arr[1], arr[0]]
            else:
                return mergeSortedArrays(mergeSort(arr[0:int(l/2)]), mergeSort(arr[int(l/2):]))

        if len(nums) < 2:
            return nums
        return mergeSort(nums)

o = Solution()
print(o.sortArray([5,1,1,2,0,0]))








