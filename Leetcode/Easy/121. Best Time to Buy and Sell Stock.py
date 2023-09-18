class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0

        minPrice = prices[0]
        maxProfit = 0

        i = 1

        while i < len(prices):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else:
                if prices[i] - minPrice > maxProfit:
                    maxProfit = prices[i] - minPrice
            i = i + 1

        return maxProfit