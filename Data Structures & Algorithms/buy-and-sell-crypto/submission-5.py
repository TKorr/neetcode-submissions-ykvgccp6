class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        maxP = 0

        while r < len(prices):
            # if sell day is > buy day, we can make profit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                # update maxP with max profit so far
                maxP = max(profit, maxP)
            else:
                # if sell day is < buy day then, we move the buy day to the sell day
                # as this is the next lowest price day
                l = r
            # move through sell days by 1 day
            r += 1
        return maxP