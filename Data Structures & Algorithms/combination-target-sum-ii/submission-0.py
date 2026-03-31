class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        def dfs(i : int, curr : List, total : int):
            if total == target:
                res.append(curr.copy())
                return
            
            if i == len(candidates) or total > target:
                return
            
            # Here we include 
            curr.append(candidates[i])
            dfs(i+1, curr, total + candidates[i])
            curr.pop()

            # loop to skip same numbers in other branch
            while (i + 1 < len(candidates) and (candidates[i] == candidates[i+1])) :
                i+=1

            dfs(i+1, curr, total)
        
        dfs(0, [], 0)
        return res
            