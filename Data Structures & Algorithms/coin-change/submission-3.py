class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                rem = i - coin
                if rem >= 0:
                    dp[i] = min(1 + dp[rem], dp[i])
        return dp[amount] if dp[amount] != amount + 1 else -1