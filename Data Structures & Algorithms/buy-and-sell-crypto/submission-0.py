class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        start = 0
        end = 1
        n = len(prices)

        while end < n:
            if prices[start] < prices[end]:
                max_profit = max(max_profit, prices[end] - prices[start])
                end += 1
            else:
                start = end
                end += 1

        return max_profit
        