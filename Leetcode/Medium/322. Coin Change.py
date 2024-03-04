import math
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if amount == 0:
            return 0

        if len(coins) == 0:
            return -1
        if len(coins) == 1:
            if coins[0] == amount:
                return amount
            elif coins[0] > amount:
                return -1

        self.r = math.inf
        self.ht = {}
        self.coins = coins

        n = coins[0]

        def dfs(a):
            if a == 0:
                return 0
            else:
                arr = []
                for c in coins:
                    if a-c >= 0:
                        if a-c in self.ht.keys():
                            arr.append(1 + self.ht[a-c])
                        else:
                            self.ht[a-c] = dfs(a-c)
                            arr.append(1 + self.ht[a-c])
                if arr != []:
                    return min(arr)
                else:
                    return math.inf
        k = dfs(amount)
        if k == math.inf:
            return -1
        else:
            return k


o = Solution()
coins = [2]
amount = 3
print(o.coinChange(coins, amount))


