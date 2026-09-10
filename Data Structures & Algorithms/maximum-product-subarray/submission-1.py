class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_min = cur_max = 1
        for n in nums:
            cur_min, cur_max = min(n, cur_min * n, cur_max * n), max(n, cur_min * n, cur_max * n)
            res = max(res, cur_max)
        return res