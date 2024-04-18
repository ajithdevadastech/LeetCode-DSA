class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 1:
            return 0

        r = [0,0]

        s = 0
        e = 1

        hist = prices[0]

        profit = 0

        while e < len(prices):
            if prices[e] >= hist:
                profit = max(profit, prices[e] - prices[s])
                hist = prices[e]
                e = e + 1
            else:
                if profit > r[1]:
                    r[0] = r[1]
                    r[1] = profit
                elif profit > r[0]:
                    r[0] = profit
                hist = prices[e]
                s = e
                e = s + 1
                profit = 0

        if profit > r[1]:
            r[0] = r[1]
            r[1] = profit
        elif profit > r[0]:
            r[0] = profit

        return r[0] + r[1]


o = Solution()
prices = [1,2,4,2,5,7,2,4,9,0]
print(o.maxProfit(prices))




