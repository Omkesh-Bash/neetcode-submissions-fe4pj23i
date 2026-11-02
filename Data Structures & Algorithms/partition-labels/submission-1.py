class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_index = {}
        for i, e in enumerate(s):
            last_index[e] = i
        
        end = size = 0
        res = []
        for i, e in enumerate(s):
            size += 1
            end = max(end, last_index[e])
            if i == end:
                res.append(size)
                size = 0
        return res