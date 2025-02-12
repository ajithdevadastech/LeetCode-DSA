class Solution(object):
    def clearDigits(self, s):

        if len(s) == 0 or len(s) == 1:
            return s

        lowercase_alphabets = [chr(i) for i in range(97, 123)]
        uppercase_alphabets = [chr(i) for i in range(65, 91)]

        s1 = []
        l = len(s)
        i = l-1
        while i >= 0:
            if s[i] in lowercase_alphabets or s[i] in uppercase_alphabets:
                if len(s1) > 0:
                    if s1[-1] not in lowercase_alphabets and s1[-1] not in uppercase_alphabets:
                        s1.pop()
                    else:
                        s1.append(s[i])
                else:
                    s1.append(s[i])
            else:
                s1.append(s[i])
            i = i - 1

        k = len(s1)
        i = k-1
        s = ""
        while i >= 0:
            s = s + s1[i]
            i = i - 1

        return s

o = Solution()
s = "cb34"
print(o.clearDigits(s))

