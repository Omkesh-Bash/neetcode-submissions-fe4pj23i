class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s, ans = 0, 1, 0
        
        while s < len(prices):
            if prices[b] < prices[s]:
                ans = max(ans, prices[s] - prices[b])
            else:
                b = s
            s+=1
            
        return ans