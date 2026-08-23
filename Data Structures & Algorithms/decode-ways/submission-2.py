class Solution:
    def numDecodings(self, s: str) -> int:
        # self.res = 0
        n = len(s)
        memo = [-1]*(n + 1)
        def dfs(i : int) -> int:
            if memo[i] != -1:
                return memo[i]
            if i == n:
                return 1
            elif s[i] == "0":
                return 0
            r1 = dfs(i + 1)
            if i + 1 < n and int(s[i: i + 2]) < 27:
                r1 += dfs(i+2)
            memo[i] = r1
            return r1
        
        return dfs(0)