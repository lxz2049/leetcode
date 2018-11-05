#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (31.83%)
# Total Accepted:    125.8K
# Total Submissions: 395.1K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
# 
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
# 
# Example 1:
# 
# 
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are
# engaging multiple transactions at the same time. You must sell before buying
# again.
# 
# 
# Example 3:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        first = [None] * len(prices)
        second = [None] * len(prices)
        low = prices[0]
        for i, p in enumerate(prices):
            low = min(low, p)
            first[i] = max(first[i-1] if i else 0, p - low)

        high = prices[-1]
        for i in xrange(len(prices) - 1, -1, -1):
            p = prices[i]
            high = max(high, p)
            second[i] = max(second[i+1] if i < len(prices) - 1 else 0, high - p)

        ret = 0
        for i, p in enumerate(prices):
            ret = max(ret, first[i] + (second[i+1] if i < len(prices) - 1 else 0))
        #print first, second
        return ret

    def test(self):
        print self.maxProfit([3,3,5,0,0,3,1,4])
        print self.maxProfit([1,2,3,4,5])
        print self.maxProfit([7,6,4,3,1])
        print self.maxProfit([3,2,6,5,0,3])
