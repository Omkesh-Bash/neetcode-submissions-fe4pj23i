class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def change(rem : int) : 
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            if rem in memo:
                return memo[rem]
            min_path = float('inf')
            for coin in coins:
                res = change(rem - coin)
                if res != float('inf'):
                    min_path = min(res + 1, min_path)
            memo[rem] = min_path
            return min_path
        res = change(amount)
        return res if res != float('inf') else -1