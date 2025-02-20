import math


class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """

        vals = {}
        used = {}

        def helper(s):
            if len(s) == len(tiles):
                return
            else:
                j = 0
                while j < len(tiles):
                    if j not in used.keys():
                        used[j] = 1
                        s = s + tiles[j]
                        if s not in vals.keys():
                            vals[s] = 1
                        helper(s)
                        #backtracking
                        s = s[:-1]
                        del used[j]
                    j = j + 1




        i = 0
        for s in tiles:
            used[i] = 1
            if s not in vals.keys():
                helper(s)
            vals[s] = 1
            used = {}
            i = i + 1

        return len(vals)


o = Solution()
tiles = "AAABBC"
print(o.numTilePossibilities(tiles))
