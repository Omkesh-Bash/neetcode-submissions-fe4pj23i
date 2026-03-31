class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        h = {}
        h2 = {}
        for c in s1:
            h2[c] = h2.get(c, 0) + 1
        for r in range(len(s2)):
            h[s2[r]] = h.get(s2[r], 0) + 1
            while r-l+1 == len(s1):
                if h == h2 :
                    return True
                else:
                    if h[s2[l]] == 1:
                        h.pop(s2[l])
                    else:
                        h[s2[l]] -= 1
                    l += 1
        return False