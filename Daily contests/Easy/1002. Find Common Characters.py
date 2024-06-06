class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        alphaarr = []
        r = []

        for word in words:
            a = [0] * 26
            for letter in word:
                k = ord(letter)
                a[ord(letter)-97] += 1
            alphaarr.append(a)

        l = len(words)

        i = 0
        while i < 26:
            j = 0
            minval = 101
            flag = True
            while j < l:
                if alphaarr[j][i] == 0:
                    flag = False
                    break
                else:
                    if alphaarr[j][i] < minval:
                        minval = alphaarr[j][i]
                j += 1
            if flag:
                k = 1
                while k <= minval:
                    r.append(chr(i+97).lower())
                    k+=1
            i += 1

        return r

o = Solution()
words = ["bella","label","roller"]
print(o.commonChars(words))





