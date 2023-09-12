class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        dictL = {}
        dictE = {}

        i = 0

        while i < len(s):
            if s[i] not in dictL.keys():
                dictL[s[i]] = t[i]
                if t[i] in dictE.keys():
                    return False
                else:
                    dictE[t[i]] = 1
            else:
                if dictL[s[i]] != t[i]:
                    return False
                else:
                    i = i + 1

        return True