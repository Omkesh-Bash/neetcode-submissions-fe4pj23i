# O(n) time with O(1)  space
class Solution:
    def numDecodings(self, s: str) -> int:
        n1, n2, n = 1, 0, len(s)
        for i in range(n -1, -1, -1):
            cur = 0
            if s[i] != '0':
                cur += n1

                if i + 1 < n and int(s[i : i + 2]) < 27:
                    cur += n2
            n1, n2 = cur, n1
        return n1