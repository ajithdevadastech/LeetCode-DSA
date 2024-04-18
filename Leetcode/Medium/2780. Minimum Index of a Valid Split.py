class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        mef = None
        rcf = 0
        histf = None
        arrf = []
        while i < len(nums):
            if histf is None or rcf == 0:
                mef = nums[i]
                rcf = 1
            elif histf != nums[i]:
                rcf = rcf - 1
            else:
                rcf = rcf + 1
            arrf.append(mef)
            histf = nums[i]
            i = i + 1

        i = len(nums) - 1
        mer = None
        rcr = 0
        histr = None
        arrr = []
        while i >= 0:
            if histr is None or rcr == 0:
                mer = nums[i]
                rcr = 1
            elif histr != nums[i]:
                rcr = rcr - 1
            else:
                rcr = rcr + 1
            arrr.append(mer)
            histr = nums[i]
            i = i - 1

        j = 0
        while j < len(arrf):
            if arrf[j] == arrr[len(nums) - 2 - j]:
                return j
            j = j + 1
        return -1

o = Solution()
nums = [3,3,3,3,7,2,2]
print(o.minimumIndex(nums))


#algorithm

#1. loop forward, capture majority element at each index and store in array1
#2. loop reverse, capture majority element at each index and store in array2
#3. loop through array1, if array1[i] = array2[i], return i

