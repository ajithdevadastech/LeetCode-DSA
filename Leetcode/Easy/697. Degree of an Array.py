import math
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 1

        dictarr = {}
        i = 0
        maxfreq = 1
        maxfreqnum = [nums[0]]

        for n in nums:
            if n not in dictarr.keys():
                dictarr[n] = [1, i, i]
            else:
                dictarr[n][0] = dictarr[n][0] + 1
                dictarr[n][2] = i
                if dictarr[n][0] == maxfreq:
                    maxfreqnum.append(n)
                elif dictarr[n][0] > maxfreq:
                    maxfreq = dictarr[n][0]
                    maxfreqnum = [n]
            i = i + 1

        if len(maxfreqnum) == 1:
            return dictarr[maxfreqnum[0]][2] - dictarr[maxfreqnum[0]][1] + 1
        else:
            r = math.inf
            for a in maxfreqnum:
                r = min(r, dictarr[a][2] - dictarr[a][1] + 1)
            return r

o = Solution()
nums = [1,2,2,3,1,4,2]
print(o.findShortestSubArray(nums))