class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #encode s
        sc = []
        dictCode = {'A':'0', 'C':'1', 'G':'2', 'T':'3'}
        i = 0
        while i < len(s):
            sc.append(dictCode[s[i]])
            i = i + 1

        k = 10

        hashVal = 0
        #hash k digits
        val = sc[0:k]
        for i in range(k):
            hashVal = hashVal + (int(val[k-1-i]) * (4**i))

        dictHash = {}
        dictHash[hashVal] = 1

        b = 0
        e = k-1

        r = []

        while True:
            if e == len(sc) - 1:
                break
            hashVal = 4 * hashVal - (int(sc[b]) * (4**(k))) + int(sc[e+1])
            if hashVal in dictHash.keys():
                if dictHash[hashVal] == 1:
                    r.append(s[(b+1):(e+2)])
                dictHash[hashVal] = dictHash[hashVal] + 1
            else:
                dictHash[hashVal] = 1
            b = b + 1
            e = e + 1

        return r

o = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(o.findRepeatedDnaSequences(s))