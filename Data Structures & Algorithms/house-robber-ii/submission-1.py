class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper_thief(lst : List[int]) -> int:
            rob1, rob2 = 0, 0
            for i in range(len(lst)):
                rob1, rob2 = rob2, max(rob2, rob1 + lst[i])
            return rob2
        return max(nums[0], helper_thief(nums[: -1]), helper_thief(nums[1 :]))