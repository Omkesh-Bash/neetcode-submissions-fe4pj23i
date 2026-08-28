from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def rob(i : int):
            if i >= n:
                return 0;
            return max(rob(i+2), rob(i+3)) + nums[i]
        return max(rob(0), rob(1))