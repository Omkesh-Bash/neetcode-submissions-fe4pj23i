class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        goal = n
        dp = [False] * (n)
        dp[n-1] = True
        for i in range(n-2, -1, -1):
            for jump in range(i+1, i+nums[i]+1):
                if jump <= goal:
                    if dp[jump]:
                        dp[i] = True
                        goal = i
                        break
        return dp[0]
