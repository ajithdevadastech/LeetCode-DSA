class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        #reference: https://www.youtube.com/watch?v=gdXkkmzvR3c

        if len(stones) == 1:
            return stones[0]

        #initialize the dp array

        self.curr = [0] * sum(stones)
        self.next = self.curr[:]

        #initialize curr
        self.curr[0] = 1
        self.curr[stones[0]] = 1

        for i in range(1, len(stones)):
            k = 0
            for j in range(sum(stones)):
                if self.curr[j] == 1:
                    if j + stones[i] < sum(stones):
                        self.next[j + stones[i]] = 1
                    self.next[j] = 1
            self.curr = self.next[:]
            self.next = [0] * sum(stones)

        i = sum(stones)//2
        t = None
        while True:
            if self.curr[i] == 1:
                t = i
                break
            else:
                i = i - 1

        return abs(t - (sum(stones)-t))

o = Solution()
stones = [31,26,33,21,40]
print(o.lastStoneWeightII(stones))