import heapq
class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        """
        0 1 2 3 4 5 6 
        4 2 3 2 4 3 1

        1. loop through all numbers as first digit
        2. populate the next higher on next if queue is empty. if queue is there, check for each elements in the queue.if not possible add that index to a queue and move on the next index
        3. if its impossible to place a number, recursively move to the next index.
        
        """

        if n == 1:
            return 1
        if n == 2:
            return [2,1,2]

        self.arr = []

        def helper(arr, n):

            if n==1:
                # self.arr = arr.copy()
                # return
                return arr
            else:
                j = 0
                while j+n < len(arr):
                    if arr[j] == 0 and arr[j+n] == 0:
                        arr[j] = n
                        arr[j+n] = n
                        if helper(arr,n-1):
                            if arr > self.arr:
                                self.arr = arr.copy()
                        arr[j] = 0
                        arr[j+n] = 0
                    j = j + 1
                return



        arr = [0] * ((2 * (n-1)) + 1)
        arr[0] = n
        arr[0+n] = n
        helper(arr,n-1)
        i = 0
        while i < len(self.arr):
            if self.arr[i] == 0:
                self.arr[i] = 1
                break
            i = i + 1
        return self.arr

o = Solution()
n = 14
print(o.constructDistancedSequence(n))

