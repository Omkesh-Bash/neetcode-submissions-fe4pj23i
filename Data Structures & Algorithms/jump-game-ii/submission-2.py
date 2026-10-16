class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        l = r = res = 0 
        while r < n-1:
            f = 0
            for i in range(l, r+1):
                f = max(f, nums[i] + i)
            l = r+1
            r = f
            res += 1
        return res