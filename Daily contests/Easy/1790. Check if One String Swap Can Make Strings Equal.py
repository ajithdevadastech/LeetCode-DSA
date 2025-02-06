class Solution(object):

    def areAlmostEqual(self, s1, s2):

        def findstring(s, Str):
            a = []
            i = 0
            while i < len(Str):
                if s == Str[i]:
                    a.append(i)
                i = i + 1
            return a


        if len(s1) != len(s2):
            return False

        j = 0
        w = 0
        while j < len(s1):
            if s1[j] == s2[j]:
                j = j + 1
            else:
                w = w + 1
                if w > 1:
                    return False
                k1 = findstring(s2[j], s1)
                flag = False
                for k in k1:
                    if s1[j] == s2[k]:
                        a2 = list(s2)
                        t = a2[j]
                        a2[j] = a2[k]
                        a2[k] = t
                        if s1 != ''.join(a2):
                            return False
                        else:
                            return True
                        flag = True
                if flag is False:
                    return False
                j = j + 1

        return True

o  = Solution()
s1 = "attack"
s2 = "ttaack"
print(o.areAlmostEqual(s1,s2))



