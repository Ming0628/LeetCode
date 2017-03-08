class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        for i in range(len(prices)):
            temp = max(map(lambda x, y: x - y, prices[i:], prices[:(len(prices) - i)]))
            maxProfit = max(temp, maxProfit)
        return maxProfit

    def maxProfit(self, prices):
        maxProfit = curMax = curindex = 0
        for i in range(len(prices) - 1, -1, -1):
            curMax = max(curindex - prices[i], curMax)
            if curindex - prices[i] < 0:
                curindex = prices[i]
            maxProfit = max(curMax, maxProfit)
        return maxProfit

    
test = Solution()
print test.maxProfit([7, 1, 5, 3, 6, 4])
print test.maxProfit([0])
print test.maxProfit([7])
print test.maxProfit([1, 2])
print test.maxProfit([1, 2, 3])
print test.maxProfit([7, 1, 5])
