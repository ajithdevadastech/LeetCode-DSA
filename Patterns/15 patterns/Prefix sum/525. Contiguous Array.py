class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dictC = {}
        r = 0
        i = 0
        c = 0
        for n in nums:
            if n == 0:
                c -= 1
            else:
                c += 1
            if c == 0:
                if i > r:
                    r = i + 1
            else:
                if c not in dictC:
                    dictC[c] = i
                else:
                    if i - dictC[c] > r:
                        r = i - dictC[c]
            i = i + 1

        return r
