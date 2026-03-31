class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights)-1
        while l < r:
            if heights[r] < heights[l]:
                area = (r-l) * heights[r]
                r-=1
            else:
                area = (r-l) * heights[l]
                l+=1
            res = max(res, area)
        return res

