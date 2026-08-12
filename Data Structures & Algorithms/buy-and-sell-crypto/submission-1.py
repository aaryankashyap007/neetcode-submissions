class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, curr, maxim = 0, 0, 0
        for i in range(len(prices)):
            if prices[i] <= prices[low]:
                low = i
                if maxim < curr:
                    maxim = curr
                curr = 0
            else:
                if prices[i] > prices[i - 1]:
                    curr = max(curr, prices[i] - prices[low])
        return max(curr, maxim)