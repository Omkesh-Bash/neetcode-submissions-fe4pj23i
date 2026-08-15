class Solution: # O(n^3)
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0

        for i in range(len(s)):
            # Odd check
            l, r = i, i
            while 0 <= l  and r < len(s) and s[l] == s[r]:
                if res_len < (r - l + 1):
                    res = s[l : r + 1]
                    res_len = len(res)
                l -= 1
                r += 1
            # Even check
            l, r = i, i + 1
            while 0 <= l  and r < len(s) and s[l] == s[r]:
                if res_len < (r - l + 1):
                    res = s[l : r + 1]
                    res_len = len(res)
                l -= 1
                r += 1
        return res