class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """

        """
        algorithm:
        -------------
        
        1. p1, p2, pointers moving past len(colors) must be modulo-ed by len(colors)
        2. extend p2 till k. if there are repeating colors, move p1 and p2 to the end and restart.
        3. if p2 moves till k without repeating colors, do sliding.
        4. if repeating color gets added on the right, set p1 and p2 to that place.
        5. end when p1 > len(colors)
        
        """

        p1 = 0
        p2 = 1
        r = 0
        i = 1
        L = len(colors)
        prev = colors[0]
        r = 0
        while True:
            p2 = p2%L

            if colors[p2] == prev:
                if p1 > p2:
                    break
                p1 = p2
                p2 = p2 + 1
                i = 1
            else:
                if i == k-1:
                    r = r + 1
                    p1 = p1 + 1
                    prev = colors[p2]
                    p2 = p2 + 1
                else:
                    i = i + 1
                    prev = colors[p2]
                    p2 = p2 + 1

            if p1 > len(colors) - 1:
                break

        return r

o = Solution()
colors = [0,1,1]
k = 3
print(o.numberOfAlternatingGroups(colors,k))




