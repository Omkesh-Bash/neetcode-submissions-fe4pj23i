class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return t

        # create hashmaps
        window, t_count = {}, {}
        # create t_count
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)

        need, have = len(t_count), 0
        res, res_len = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # if that char increases have
            if c in t_count and window[c] == t_count[c]:
                have +=1

            # if substring found
            while need == have:
                if r-l+1 < res_len:
                    res = [l, r]
                    res_len = r-l+1
                    
                # remove char form l
                window[s[l]] -=1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have-=1
                l+=1

        return s[res[0] : res[1]+1] if res_len != float("infinity") else ''