class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        self.dp = [0] * (amount+1)
        self.dp[0] = 1

        for coin in coins:
            for j in range(coin, amount+1):
                self.dp[j] = self.dp[j] + self.dp[j-coin]

        return self.dp[amount]


o = Solution()
amount = 3
coins = [2]
print(o.change(amount, coins))

