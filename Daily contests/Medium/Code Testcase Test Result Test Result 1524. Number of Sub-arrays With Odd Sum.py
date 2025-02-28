class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        if len(arr) == 1:
            if arr[0]%2 > 0:
                return 1
            else:
                return 0

        currSum = 0
        oddpf = 0
        evenpf = 0
        r = 0

        i = 0
        while i < len(arr):
            currSum = currSum + arr[i]
            if currSum % 2 > 0:
                r = r + 1
                r = r + evenpf
                oddpf = oddpf + 1
            else:
                r = r + oddpf
                evenpf = evenpf + 1
            i = i + 1
        return r

o = Solution()
arr = [2,4,6]
print(o.numOfSubarrays(arr))
