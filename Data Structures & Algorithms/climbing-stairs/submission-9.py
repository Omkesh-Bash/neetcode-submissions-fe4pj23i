class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        n1, n2 = 2, 1
        for i in range(n-3):
            n1, n2 = n1 + n2, n1
        return n1 + n2