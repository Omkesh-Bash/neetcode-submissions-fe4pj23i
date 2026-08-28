class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cur, n1, n2, n3 = nums[-2], nums[-1], 0, 0
        for i in range(len(nums)-3, -1, -1):
            cur, n1, n2, n3 = max(n2, n1) + nums[i], cur, n1, n2
        return max(cur, n1)