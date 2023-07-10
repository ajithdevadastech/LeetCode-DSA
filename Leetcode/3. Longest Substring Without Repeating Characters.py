class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0 or len(s) == 1:
            return len(s)

        maxL = 0
        b = 0
        d = {}

        for e in range(len(s)):
            if s[e] in d:
                b = max(b, d[s[e]])
            maxL = max(maxL, e-b+1)
            d[s[e]] = e+1


        return maxL





o = Solution()

s = "tmmzuxt"


print(o.lengthOfLongestSubstring(s))