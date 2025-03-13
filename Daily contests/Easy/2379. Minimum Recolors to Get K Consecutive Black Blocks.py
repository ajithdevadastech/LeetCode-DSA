class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """

        """
        algorithm
        --------------
        
        1. create a window of size k and count Ws
        2. slide through the arr
            2.1. if remove = W and add = B, decrement the result
        3. return result
        
        """

        if k == len(blocks):
            #return Ws
            r = 0
            for b in blocks:
                if b == 'W':
                    r = r + 1
            return r

        i = 0
        r = 0
        while i < k:
            if blocks[i] == 'W':
                r = r + 1
            i = i + 1

        p1 = 0
        p2 = k-1
        minval = r
        while p2+1 < len(blocks):
            if blocks[p1] == 'W' and blocks[p2+1] == 'B':
                r = r - 1
            if blocks[p1] == 'B' and blocks[p2+1] == 'W':
                r = r + 1
            if r < minval:
                minval = r
            p1 = p1 + 1
            p2 = p2 + 1

        return minval

o = Solution()
blocks = "BBBBBWWBBWBWBWWWBWBWBBBBWBBBBWBWBWBWBWWBWWBWBWWWWBBWWWWBWWWWBWBBWBBWBBWWW"
k = 29
print(o.minimumRecolors(blocks,k))

