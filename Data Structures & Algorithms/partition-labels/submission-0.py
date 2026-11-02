class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        last_location_map = {}
        for i in range(n-1, -1, -1):
            if s[i] not in last_location_map:
                last_location_map[s[i]] = i
        # return last_location_map

        end = size = 0
        i = 0
        res = []
        while i < n:
            size += 1
            # print(size, i)
            if last_location_map[s[i]] > end:
                end = last_location_map[s[i]]
            if i == end:
                res.append(size)
                size = 0
            i += 1
        return res