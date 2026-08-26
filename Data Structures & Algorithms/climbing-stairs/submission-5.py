class Solution:
    # Memo
    def climbStairs(self, n: int) -> int:
        memo = [0]*(n+1)
        def backtrack(i: int) -> int:
            if i == n: 
                return 1
            if i > n: # invalid
                return 0
            if memo[i] != 0:
                return memo[i]
            curr = backtrack(i + 1) + backtrack(i + 2)
            memo[i] = curr 
            return curr
        backtrack(0)
        return memo[0]