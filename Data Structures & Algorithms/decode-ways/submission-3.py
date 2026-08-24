# O(n) solution bottom up
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [0] * (n + 1)
        memo[n] = 1 # only one combination for last one "" empty string 

        for i in range(n - 1, -1 , -1):
            if s[i] == '0':
                continue
            memo[i] = memo[i+1]
            if i + 1 < n and int(s[i : i + 2]) < 27:
                memo[i] += memo[i + 2]
        return memo[0]