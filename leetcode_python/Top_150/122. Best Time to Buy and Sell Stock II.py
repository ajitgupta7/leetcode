class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        buy = prices[0]

        for sell in prices[1:]:

            if sell > buy:
                profit += sell - buy
                buy = sell
            else:
                buy = sell

        return profit