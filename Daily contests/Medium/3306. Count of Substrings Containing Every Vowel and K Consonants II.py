class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """

        """
        c - c -> move both sides 1 step and increment
        c - v -> move left 1 step, move right until we find a 'c', increment
        v - c -> if val == 0, move right until we find the same v, increment. if val!= 0, increment, move left 1 step  and start from step 1
        v - v -> if v = v, move both sides 1 step and increment. 
                 if not, if val == 0, move right until we find the same v, increment. if val!= 0, increment, move left 1 step  and start from step 1
        """

        r = 0

        dictVowels = {}
        dictVowels['a'] = 0
        dictVowels['e'] = 0
        dictVowels['i'] = 0
        dictVowels['o'] = 0
        dictVowels['u'] = 0

        def haveallvowels():
            for v in dictVowels.values():
                if v == 0:
                    return False
            return True

        #find a valid string first
        flag = False
        cCount = 0
        i = 0
        for w in word:
            if w in dictVowels.keys():
                dictVowels[w] = dictVowels[w] + 1
            else:
                cCount = cCount + 1
            if haveallvowels():
                if cCount == k:
                    r = r + 1
                    flag = True
                    break

            i = i + 1

        if flag is False:
            return r

        #sliding window logic

        p1 = 0
        p2 = i

        while p2+1 < len(word):
            m = word[p1]
            a = word[p2+1]
            if m not in dictVowels.keys() and a not in dictVowels.keys():
                r = r + 1
                p1 = p1 + 1
                p2 = p2 + 1
            elif m not in dictVowels.keys() and a in dictVowels.keys():
                p1 = p1 + 1
                while p2+1 < len(word):
                    if word[p2+1] in dictVowels.keys():
                        dictVowels[word[p2+1]] = dictVowels[word[p2+1]] + 1
                    else:
                        r = r + 1
                        p2 = p2 + 1
                        break
                    p2 = p2 + 1
            elif m in dictVowels.keys() and a not in dictVowels.keys():
                if dictVowels[m] == 1:
                    dictVowels[m] = 0
                    p1 = p1 + 1
                    while p2 + 1 < len(word):
                        if word[p2 + 1] in dictVowels.keys():
                            dictVowels[word[p2+1]] = dictVowels[word[p2+1]] + 1
                            if word[p2+1] == m:
                                r = r + 1
                                p2 = p2 +1
                                break
                            else:
                                p2 = p2 + 1
                        else:
                            cCount = cCount + 1
                            p2 = p2 + 1
                else:
                    p1 = p1 + 1
            else:
                if m == a:
                    r = r + 1
                    p1 = p1 + 1
                    p2 = p2 + 1
                else:
                    if dictVowels[m] == 1:
                        dictVowels[m] = 0
                        p1 = p1 + 1
                        while p2 + 1 < len(word):
                            if word[p2 + 1] in dictVowels.keys():
                                dictVowels[word[p2 + 1]] = dictVowels[word[p2 + 1]] + 1
                                if word[p2 + 1] == m:
                                    r = r + 1
                                    p2 = p2 + 1
                                    break
                                else:
                                    p2 = p2 + 1
                            else:
                                cCount = cCount + 1
                                p2 = p2 + 1
                    else:
                        p1 = p1 + 1

        return r

o = Solution()
word = "ieaouqqieaouqq"
k = 1
print(o.countOfSubstrings(word,k))














