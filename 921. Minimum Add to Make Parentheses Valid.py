class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        total = 0
        bal = 0

        for p in s:
            if p == '(':
                total = total + 1

            if p == ')':
                if total > 0:
                    total = total - 1
                else:
                    bal = bal + 1

        return total + bal

o = Solution()
s = "((("
print(o.minAddToMakeValid(s))



