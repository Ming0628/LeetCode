class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        else:
            length = len(prices)
            maxProfit = curProfit = 0
            for i in range(length - 1, 0, -1):
                curProfit = max(curProfit, curProfit + (prices[i] - prices[i - 1]))
                maxProfit = max(curProfit, maxProfit)
            return maxProfit


test = Solution()
print test.maxProfit([7, 1, 5, 3, 6, 4, 5])
