
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(s) < len(t):
            return ""


        #create index arr and value arr

        valArr = []
        indexArr = []

        tDict = {}
        for j in t:
            if j in tDict.keys():
                tDict[j] = tDict[j] + 1
            else:
                tDict[j] = 1

        i=0
        while i < len(s):
            if s[i] in tDict.keys():
                indexArr.append(i)
                valArr.append(s[i])
            i = i + 1

        if len(valArr) == 0:
            return ""

        def check (d):
            flag = 'best'
            for a in tDict.keys():
                if a not in d.keys():
                    return 'worst'
                else:
                    if d[a] < tDict[a]:
                        return 'worst'
                    elif d[a] > tDict[a]:
                        flag = 'ok'
            return flag

        def removechar (char, d):
            if char in d.keys():
                if d[char] == 1:
                    del d[char]
                else:
                    d[char] = d[char] - 1
            return d

        def addchar(char,d):
            if char in d.keys():
                d[char] = d[char] + 1
            else:
                d[char] = 1
            return d

        # find the first full series

        p1 = 0
        p2 = 0
        loopDict = {}
        minWindowval = float('inf')
        minwindowrange = []
        while True:
            if p2 > len(valArr) - 1:
                return ""
            if valArr[p2] not in loopDict.keys():
                loopDict[valArr[p2]] = 1
            else:
                loopDict[valArr[p2]] = loopDict[valArr[p2]] + 1

            if p2 >= len(t) - 1:
                k = check(loopDict)
                if k == 'best' or k == 'ok':
                    if indexArr[p2]-indexArr[p1]+1 < minWindowval:
                        minWindowval = indexArr[p2]-indexArr[p1]+1
                        minwindowrange = [indexArr[p1],indexArr[p2]]
                    break
            p2 = p2 + 1

        while True:
            x = check(loopDict)
            if x == 'ok':
                if indexArr[p2]-indexArr[p1]+1 < minWindowval:
                    minWindowval = indexArr[p2]-indexArr[p1]+1
                    minwindowrange = [indexArr[p1],indexArr[p2]]
                c = valArr[p1]
                loopDict = removechar(c, loopDict)
                p1 = p1 + 1
            elif x == 'worst':
                p2 = p2 + 1
                if p2 >= len(valArr):
                    break
                loopDict = addchar(valArr[p2], loopDict)
            else:
                if indexArr[p2]-indexArr[p1]+1 < minWindowval:
                    minWindowval = indexArr[p2]-indexArr[p1]+1
                    minwindowrange = [indexArr[p1],indexArr[p2]]
                c = valArr[p1]
                loopDict = removechar(c, loopDict)
                p1 = p1 + 1
                p2 = p2 + 1
                if p2 >= len(valArr):
                    break
                loopDict = addchar(valArr[p2], loopDict)

        return s[minwindowrange[0]:minwindowrange[1]+1]


o = Solution()
s = "acbbaca"
t = "aba"
print(o.minWindow(s,t))









