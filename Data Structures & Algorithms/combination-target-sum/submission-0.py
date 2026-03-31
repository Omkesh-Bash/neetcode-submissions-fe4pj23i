class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, curr : List, total):
            if total == target:
                res.append(curr.copy())
                return
            if i == len(candidates) or total > target:
                return

            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i]) # decision where ith value is always included

            curr.pop() 
            dfs(i+1, curr, total)  # decision where ith value is always excluded

        dfs(0, [], 0)
        return res