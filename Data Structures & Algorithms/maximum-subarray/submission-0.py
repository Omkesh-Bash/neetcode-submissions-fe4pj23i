class Solution:
    def maxSubArray(self, nums: List[int]) -> bool:
        res = nums[0]
        cur = 0
        for n in nums:
            cur = cur + n
            res = max(res, cur)
            if cur < 0:
                cur = 0
        return res