# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution_1:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        max_profit = 0
        for i in range(len(prices) - 1):
            if prices[buy] < prices[sell]:
                curr_profit = prices[sell] - prices[buy]
                max_profit = max(curr_profit, max_profit)
            else:
                buy = sell
            sell += 1

        return max_profit


input_prices = [1,2,4,2,5,7,2,4,9,0,9]
solve = Solution_1()
print(solve.maxProfit(input_prices))
