class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [False] * (n)
        dp[n-1] = True
        for i in range(n-2, -1, -1):
            for jump in range(i+1, i+nums[i]+1):
                if jump < n:
                    if dp[jump]:
                        dp[i] = True
                        break
        return dp[0]