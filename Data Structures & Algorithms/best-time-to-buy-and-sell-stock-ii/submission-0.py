class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = [0] * len(prices)
        for i in range(1, len(arr)):
            arr[i] = prices[i] - prices[i - 1]
        
        ans = 0
        for num in arr:
            if num >= 0:
                ans += num
        
        return ans