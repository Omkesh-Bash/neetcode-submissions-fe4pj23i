class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, count = 0, 0, 0
        sett = set()
        while r < len(s):
            if s[r] in sett:
                count = max(count, r-l)
                l +=1
                r = l
                sett.clear()
                # print(l ," ", r)
            else:
                sett.add(s[r])
                r+=1
        count = max(count, r-l)
        return count