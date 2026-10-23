class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        matched = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, val in enumerate(t):
                if val == target[i]:
                    matched.add(i)
            if len(matched) == 3:
                return True
        return False