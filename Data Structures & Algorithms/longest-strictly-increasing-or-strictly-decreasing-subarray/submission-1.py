
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        res = 0
        i = 0
        while i < len(nums)-1:
            cur = 0
            j = i
            while i < len(nums)-1 and nums[i] < nums[i + 1]:
                i += 1
            res = max(res, i - j + 1)
            i += 1

        i = 0
        while i < len(nums)-1:
            cur = 0
            j = i
            while i < len(nums)-1 and nums[i] > nums[i + 1]:
                i += 1
            res = max(res, i - j + 1)
            i += 1
        return res