class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 2)
        memo[n] = 1
        for i in range(n-1, -1, -1):
            memo[i] = memo[i+1] + memo[i+2]
        return memo[0]