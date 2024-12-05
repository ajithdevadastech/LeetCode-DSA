class Solution(object):
    def numberOfWays(self, startPos, endPos, k):
        """
        :type startPos: int
        :type endPos: int
        :type k: int
        :rtype: int
        """
        self.memo = {}
        def helper(val, hop):
            if hop == k:
                if val == endPos:
                    return 1
                else:
                    return 0
            else:
                if val in self.memo.keys():
                    return self.memo[(val,hop)]
                else:
                    self.memo[(val,hop)] = helper(val-1, hop+1) + helper(val+1, hop+1)
                    return self.memo[(val,hop)]

        return helper(startPos, 0)

o = Solution()
startPos = 1
endPos = 1000
k = 998
print(o.numberOfWays(startPos, endPos, k))
