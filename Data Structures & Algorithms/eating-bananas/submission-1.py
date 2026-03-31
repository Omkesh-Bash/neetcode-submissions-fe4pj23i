class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        res = max(piles)
        l, r = 1, res-1
        while l<=r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h: # if exact h so =
                res = min(res, k)
                r = k-1
            else:
                l = k+1
        return res