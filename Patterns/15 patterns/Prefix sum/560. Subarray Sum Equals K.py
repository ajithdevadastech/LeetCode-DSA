class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        r = 0
        dictC = {}

        i = 0
        c = 0

        for n in nums:
            if c + n - k == 0:
                r = r + 1
            elif c + n - k in dictC.keys():
                r = r + 1
            dictC[c + n] = i

            c = c + n

            i = i + 1

        return r
