class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(coins) == 0:
            return 0
        # 状态
        dp = [float('inf')] * (amount + 1)
        # 初始化
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i-coin < 0:
                    continue
                dp[i] = min(dp[i], 1+dp[i-coin])

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
