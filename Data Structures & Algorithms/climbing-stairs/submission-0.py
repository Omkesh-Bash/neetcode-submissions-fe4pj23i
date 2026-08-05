class Solution:
    def climbStairs(self, n: int) -> int:
        one = two = 1

        for _ in range(n-1): # for 5 we shift 4 times
            one, two = one + two, one
        return one