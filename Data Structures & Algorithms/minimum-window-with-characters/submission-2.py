class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return t
        w, t_c = {}, {}
        for c in t:
            t_c[c] = 1 + t_c.get(c, 0)
        n, h = len(t_c), 0
        res, res_l = 0, 100001
        l = 0
        for r in range(len(s)):
            c = s[r]
            w[c] = 1 + w.get(c, 0)
            if c in t_c and w[c] == t_c[c]:
                h +=1
            while n == h:
                if r-l+1 < res_l:
                    res = [l, r]
                    res_l = r-l+1
                w[s[l]] -=1
                if s[l] in t_c and w[s[l]] == t_c[s[l]] -1:
                    h-=1
                l+=1
        return s[res[0] : res[1]+1] if res_l != 100001 else ''