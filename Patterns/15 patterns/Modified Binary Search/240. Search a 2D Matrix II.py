class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if target < matrix[0][0]:
            return False

        def binarySearch(arr, target):
            s = 0
            e = len(arr) - 1
            while True:
                if target > arr[(s + e)//2]:
                    s = (s+e)//2
                elif target < arr[(s + e)//2]:
                    e = (s+e)//2
                else:
                    return True, (s + e)//2

                if s == e - 1 or s == e:
                    if arr[s] == target or arr[e] == target:
                        return True, 0
                    else:
                        return False, e
        def formRowarr(r, rstart, cstart):
            if rstart > nRows - 1  or cstart > nCols - 1:
                return []
            arr = []
            i = rstart
            while i <= r:
                arr.append(matrix[i][cstart])
                i = i + 1
            return arr

        nRows = len(matrix)
        nCols = len(matrix[0])

        if nRows == 1:
            f, v = binarySearch(matrix[0], target)
            return f
        if nCols == 1:
            a = formRowarr(nRows-1, 0, 0)
            f, v = binarySearch(a, target)
            return f

        rstart = 0
        cstart = 0
        rindex = nRows
        cindex = nCols
        while True:
            t1 = formRowarr(rindex+rstart-1, rstart, cstart)
            if len(t1) == 0:
                return False
            rflag, rindex = binarySearch(t1, target)
            if rflag:
                return rflag
            t2 = matrix[rstart][cstart:cindex+cstart]
            if len(t2) == 0:
                return False
            cflag, cindex = binarySearch(t2, target)
            if cflag:
                return cflag
            rstart = rstart + 1
            cstart = cstart + 1
            if rstart > nRows - 1 and cstart > nCols - 1:
                break
        return False

o = Solution()
matrix = [[4,5],[4,6],[9,14],[10,15]]
target = 6
print(o.searchMatrix(matrix, target))









