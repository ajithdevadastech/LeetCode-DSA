class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # build arrays

        ai = 0  # ascending iterator
        di = 0  # descending iterator

        i = 0  # string iterator

        logic = "asc"  # can take asc & desc

        arrgrp = []

        arr = [0] * numRows

        while i < len(s):
            if logic == "asc":
                if ai < numRows:
                    arr[ai] = s[i]
                    ai = ai + 1
                    i = i + 1
                else:
                    arrgrp.append(arr)
                    logic = "desc"
                    di = numRows - 2
                    ai = 0
                    arr = [0] * numRows
            else:
                if di > 0:
                    arr[di] = s[i]
                    i = i + 1
                    arrgrp.append(arr)
                    arr = [0] * numRows
                    di = di - 1
                else:
                    logic = "asc"
                    ai = 0
                    di = 0
                    arr = [0] * numRows

        arrgrp.append(arr)
        # read arrays

        i = 0
        j = 0

        r = ""
        while j < numRows:
            while i < len(arrgrp):
                if arrgrp[i][j] != 0:
                    r = r + arrgrp[i][j]
                i = i + 1
            i = 0
            j = j + 1

        return r

o = Solution()
s = "PAYPALISHIRING"
numRows = 4
print(o.convert(s, numRows))