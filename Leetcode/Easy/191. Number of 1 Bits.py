class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''
        do bitwise AND of the number with a bit set on 31 positions (1 << i)
        
        '''
        count = 0
        i = 0
        while i < 32:
            if n & (1 << i) > 0:
                count = count + 1
            i = i + 1

        return count

o = Solution()
n = 13
print(o.hammingWeight(n))