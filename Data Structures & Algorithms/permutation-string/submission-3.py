class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        h = dict()
        h1 = dict()
        for i in range(len(s1)):
            h[s1[i]] = h.get(s1[i], 0)+1
            h1[s2[i]] = h1.get(s2[i], 0)+1
        m = 26
        for c in h.keys():
            if h[c] != h1.get(c, 0):
                m-=1
        for i in h1.keys() - h.keys():
            if h1[i] != h.get(i, 0):
                m-=1

        for r in range(len(s1), len(s2)):
            if m == 26:return True
            h1[s2[r]] = h1.get(s2[r], 0) + 1
            if h1[s2[r]] == h.get(s2[r], 0):
                m+=1
            elif h1[s2[r]] -1 == h.get(s2[r], 0):
                m-=1

            h1[s2[l]] = h1.get(s2[l], 0) - 1
            if h1[s2[l]] == h.get(s2[l], 0):
                m+=1
            elif h1[s2[l]] +1 == h.get(s2[l], 0):
                m-=1

            l+=1
            

        return m == 26
