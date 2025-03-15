class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        p1 = 0
        p2 = 0
        r = 0

        def checkletters(st):
            if 'a' in st and 'b' in st and 'c' in st:
                return True
            return False

        while p2 < len(s):
            if checkletters(s[p1:p2+1]):
                r = r + len(s) - p2
                p1 = p1 + 1
                while True:
                    if checkletters(s[p1:p2+1]):
                        break
                    elif p2 >= len(s):
                        break
                    else:
                        p2 = p2 + 1
            else:
                p2 = p2 + 1

        return r


o = Solution()
s = "abc"
print(o.numberOfSubstrings(s))





