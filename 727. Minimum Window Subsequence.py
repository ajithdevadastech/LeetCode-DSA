class Solution(object):
    def minWindow(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: str
        """
        if len(s1) == 0:
            return ""
        if len(s2) == 0:
            return ""

        f = 0 #first index
        e = 0 #last index

        searchElem = s2[0]
        startElem = s2[0]

        i = 0 #search loop variable for s1
        j = 0 #search loop variable for s2

        dictS2 = {}

        sindex = 0
        eindex = 0

        #identifying first block
        while True:
            if i > len(s1) - 1:
                return ""
            if s1[i] == startElem:
                sindex = i
                dictS2 = {}
                dictS2[startElem] = 1
                j = 0
                j = j + 1
                if j < len(s2):
                    i = i + 1
                    searchElem = s2[j]
                else:
                    return ""
            elif s1[i] != searchElem:
                i = i + 1
            else:
                dictS2[searchElem] = 1
                j = j + 1
                if j < len(s2):
                    i = i + 1
                    searchElem = s2[j]
                elif sum(dictS2.values()) == len(s2) and s1[i] == s2[-1]:
                    eindex = i
                    break
                else:
                    return ""





        return [sindex, eindex]

o = Solution()
#s1 = "abcdebdde"
s1 = "abccbxddebdde"
s2 = "bde"
print(o.minWindow(s1, s2))









