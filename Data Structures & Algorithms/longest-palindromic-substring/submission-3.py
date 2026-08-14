class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        res = (1, s[0])

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    if j - i > res[0]:
                        res = (j - i, s[i:j])

        return res[1]