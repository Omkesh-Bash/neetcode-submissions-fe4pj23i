class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy()) # important, or else the main subset is always modified
                return
            
            # If we accept current element
            subset.append(nums[i])
            dfs(i+1)
            
            # If we reiect current element
            subset.pop()
            dfs(i+1) # this will work because first dfs of accept is completely executed and then this one

        dfs(0)
        return res