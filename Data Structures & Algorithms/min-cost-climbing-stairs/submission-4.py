class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [0] * (n+1)
        memo[n-1] = cost[-1]
        for i in range(n-2, -1, -1):
            memo[i] = min(memo[i+1], memo[i+2]) + cost[i]
        return min(memo[0],memo[1])