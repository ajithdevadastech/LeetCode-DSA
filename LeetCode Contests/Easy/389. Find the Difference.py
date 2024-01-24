class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        dictS = {}

        for i in s:
            if i in dictS.keys():
                dictS[i] += 1
            else:
                dictS[i] = 1

        for j in t:
            if j not in dictS.keys():
                return j
            else:
                dictS[j] -= 1

        for k in dictS.keys():
            if dictS[k] < 0:
                return k

s = 'a'
t = 'aa'

o = Solution()
print(o.findTheDifference(s,t))