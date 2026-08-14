class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = (0,s[0])
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i:j] == s[j:i:-1]:
                    if j - i > res[0]:
                        res = (j-i, s[i:j+1])
        return res[1]