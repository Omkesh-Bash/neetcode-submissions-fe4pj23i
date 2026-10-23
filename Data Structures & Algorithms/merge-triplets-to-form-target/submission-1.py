class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        flags = [0, 1, 2]
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i in flags.copy():
                if t[i] == target[i]:
                    flags.remove(i)
        return len(flags) == 0