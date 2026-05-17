class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProf = 0

        while right < len(prices):
            if prices[left] < prices[right]: # if left pointer price is less(TO BUY)
                profit = prices[right] - prices[left]
                maxProf = max(maxProf, profit)
            else:  # if right pointer is less...
                left = right # update the left pointer all the way to right, as becoz we found the min pointer here...
            
            right += 1 # update the right pointer to have high price(TO SELL), this will give high profit.

        return maxProf