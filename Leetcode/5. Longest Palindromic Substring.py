class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 0 or len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        ##len(s) > 2

        def expandPal (L, R):
            while L >= 0 and R < len(s) and s[L] == s[R]:
                L = L - 1
                R = R + 1
            return R-L-1

        start = 0
        end = 0

        for i in range(len(s)):
            len1 = expandPal(i, i)
            len2 = expandPal(i, i+1)
            lenF = max(len1, len2)
            if lenF >= (end - start + 1):
                if lenF % 2 == 0:
                    start = max(0, i - int((lenF-2)/2))
                    end = min(len(s)-1, int(i + 1 + (lenF-2)/2))
                else:
                    start = max(0, i - int((lenF-1)/2))
                    end = min(len(s)-1, int(i + (lenF-1)/2))

        return s[start:end+1]

o = Solution()

s = "cbbd"

print(o.longestPalindrome(s))
