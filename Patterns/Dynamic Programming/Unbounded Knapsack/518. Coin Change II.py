class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        if len(coins) == 1:
            if coins[0] == amount:
                return 1
            else:
                return 0

        self.dp = [0] * (amount+1)
        self.dp[0] = 0

        for i in range(1,amount+1):
            for j in range(len(coins)):
                if i == coins[j]:
                    self.dp[i] = self.dp[i] + 1
                elif i - coins[j] >= 0:
                    self.dp[i] = self.dp[i - coins[j]] + self.dp[i]

        return self.dp[amount]


o = Solution()
amount = 5
coins = [1,2,5]
print(o.change(amount, coins))

