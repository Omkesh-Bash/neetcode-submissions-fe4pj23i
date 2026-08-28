class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n1, n2 = cost[-1], 0
        for i in range(len(cost)-2, -1, -1):
            n1, n2 = min(n1, n2) + cost[i], n1
        return min(n1, n2)