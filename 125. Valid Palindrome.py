
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        newString = ""

        for c in s:
            if c.isalnum():
                newString += c.lower()

        l = len(newString)

        i = 0
        j = l-1

        while i < j:
            if newString[i] != newString[j]:
                return False
            i = i + 1
            j = j - 1

        return True

o = Solution()
# s = "A man, a plan, a canal: Panama"
# s = "race a car"

s = ""
print(o.isPalindrome(s))

