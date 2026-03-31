class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, count = 0, 0
        sett = set()
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            sett.add(s[r])
            count = max(count, r-l+1)
        return count