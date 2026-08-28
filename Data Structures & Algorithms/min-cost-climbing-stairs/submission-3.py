from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        @cache
        def helper(i):
            if i >= n:
                return 0
            s = min(helper(i+1), helper(i+2)) + cost[i]
            return s
        return min(helper(0), helper(1))