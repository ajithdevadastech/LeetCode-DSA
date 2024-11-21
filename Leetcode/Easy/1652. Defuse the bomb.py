import math


class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """

        quo = math.floor(abs(k) / len(code))
        rem =  abs(k) % len(code)
        sumArr = sum(code)

        if k < 0:
            direction = 'Backward'
        else:
            direction = 'Forward'

        def valueToAdd(index, direction):
            if direction == 'Forward':
                if index + rem <= len(code) - 1:
                    return code[index + rem]
                else:
                    return code[index + rem - len(code)]
            else:
                return code[index - rem]

        #calculate first element

        r = []
        s = sumArr * quo
        if direction == 'Forward':
            i = 1
            while i <= rem:
                s = s + code[i]
                i = i + 1
            r.append(s)
        else:
            i = len(code) - 2
            j = 1
            while j <= rem:
                s = s + code[i]
                i = i - 1
                j = j + 1
            r.append(s)

        #populate the remaining values:
        if direction == 'Forward':
            m = 1
            while m <= len(code) - 1:
                res = r[-1]
                s = res - code[m] + valueToAdd(m,direction)
                r.append(s)
                m = m + 1
        else:
            m = len(code) - 2
            while m >= 0:
                res = r[-1]
                s = res - code[m] + valueToAdd(m,direction)
                r.append(s)
                m = m - 1

        if direction == 'Forward':
            return r
        else:
            return r[::-1]



o = Solution()
code = [2,4,9,3]
k = -2
print(o.decrypt(code,k))
















