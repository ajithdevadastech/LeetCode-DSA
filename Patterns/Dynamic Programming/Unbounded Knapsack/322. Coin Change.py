class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        #using DP array

        self.dp = [float('inf')] * (amount+1)
        self.dp[0] = 0

        for i in range(1, amount+1):
            for j in range(len(coins)):
                if coins[j] == i:
                    self.dp[i] = 1
                elif i-coins[j] >= 0:
                    if self.dp[i - coins[j]] + 1 < self.dp[i]:
                        self.dp[i] = self.dp[i - coins[j]] + 1

        if self.dp[amount] == float('inf'):
            return -1
        else:
            return self.dp[amount]


o = Solution()
coins = [1]
amount = 0
print(o.coinChange(coins,amount))







