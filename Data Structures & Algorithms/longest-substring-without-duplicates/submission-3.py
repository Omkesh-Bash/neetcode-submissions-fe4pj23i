class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, count = 0, 0, 0
        sett = set()
        while r < len(s):
            
            if s[r] in sett:
                count = max(count, r-l)
                while s[r] in sett:
                     sett.remove(s[l])
                     l+=1
            else:
                sett.add(s[r])
                r+=1
        count = max(count, r-l)
        return count