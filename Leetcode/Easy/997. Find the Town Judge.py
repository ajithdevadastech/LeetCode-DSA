class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """

        IN = []
        OUT = []


        rOUT = -1

        for i in range(n):
            IN.append(0)
            OUT.append(0)

        for t in trust:
            OUT[t[0] - 1] = OUT[t[0] - 1] + 1
            IN[t[1] - 1] = IN[t[1] - 1] + 1

        i = 0
        while i < len(OUT):
            if OUT[i] == 0:
                rOUT = i + 1
            i = i + 1

        if rOUT != -1:
            if IN[rOUT-1] == n-1:
                return rOUT

        return -1


n = 3
trust = [[1,3],[2,3]]

o =  Solution()
print(o.findJudge(n,trust))

