class Solution(object):
    def removeOccurrences(self, s, part):

        if part == "":
            return s
        if s == "":
            return s

        if len(part) > len(s):
            return s


        s1 = []
        s2 = []

        #populate s1 with s
        l = len(s)
        i = l - 1
        while i >= 0:
            s1.append(s[i])
            i = i - 1

        while True:
            if len(s2) == 0:
                i = 0
            else:
                if s2[-1][0] == 0:
                    i = 0
                else:
                    i = s2[-1][0]
            while i < len(part):
                if s1[-1] == part[i]:
                    s2.append([i+1, s1[-1]])
                    s1.pop()
                else:
                    if s1[-1] == part[0]:
                        s2.append([1 ,s1[-1]])
                    else:
                        if len(s2) > 0:
                            if s2[-1][1] == part[0]:
                                s2[-1][0] = 1
                                s2.append([2, s1[-1]])
                            else:
                                s2.append([0, s1[-1]])
                        else:
                            s2.append([0, s1[-1]])
                    s1.pop()
                    break
                i = i + 1
                if len(s1) == 0:
                    break
            if i == len(part):
                k = 0
                while k < i:
                    s2.pop()
                    k = k + 1
            if len(s1) == 0:
                break

        a = 0
        s = ""
        while a < len(s2):
            s = s + s2[a][1]
            a = a + 1

        return s

o = Solution()
# s = "daabcbaabcbc"
# part = "abc"

# s = "axxxxyyyyb"
# part = "xy"

# s = "yjyjqnaxlbqnaxlbfss"
# part = "yjqnaxlb"

# s = "qtbxqtbxelkekgcdnelkeqtbxelkekgcdnqtbxelkekgcdnkgcdnwqchzunbvyjoq"
# part = "qtbxelkekgcdn"

# s = "kpygkivtlqoockpygkivtlqoocssnextkqzjpycbylkaondsskpygkpygkivtlqoocssnextkqzjpkpygkivtlqoocssnextkqzjpycbylkaondsycbylkaondskivtlqoocssnextkqzjpycbylkaondssnextkqzjpycbylkaondshijzgaovndkjiiuwjtcpdpbkrfsi"
# part = "kpygkivtlqoocssnextkqzjpycbylkaonds"

# s = "kpygkivtlqoocskpygkpygkivtlqoocssnextkqzjpycbylkaondskivtlqoocssnextkqzjpycbylkaondssnextkqzjpycbylkaondshijzgaovndkjiiuwjtcpdpbkrfsi"
# part = "kpygkivtlqoocssnextkqzjpycbylkaonds"

print(o.removeOccurrences(s,part))








