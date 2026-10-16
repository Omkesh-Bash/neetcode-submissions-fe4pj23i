class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * (len(nums)) # inf means not reachable
        dp[n-1] = 0
        for i in range(n - 2, -1, -1):
            for jump in range(i+nums[i], i, -1): # Given constrants are good
                if jump < n:
                    dp[i] = min(dp[jump] + 1, dp[i])
        return dp[0]