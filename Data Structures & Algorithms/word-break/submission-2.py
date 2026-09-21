class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                end = i + len(word)
                if end <= n and s[i : end] == word:
                    if dp[end]:
                        dp[i] = dp[end]
                        break

        return dp[0]
                    