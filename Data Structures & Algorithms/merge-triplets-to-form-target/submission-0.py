class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        # selected = []
        flags = [False, False, False]
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            if not flags[0] and t[0] == target[0]:
                flags[0] = True
            if not flags[1] and t[1] == target[1]:
                flags[1] = True
            if not flags[2] and t[2] == target[2]:
                flags[2] = True
        return sum(flags) == 3