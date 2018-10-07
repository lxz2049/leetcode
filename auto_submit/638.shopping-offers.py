#
# [638] Shopping Offers
#
# https://leetcode.com/problems/shopping-offers/description/
#
# algorithms
# Medium (46.25%)
# Total Accepted:    15.5K
# Total Submissions: 33.6K
# Testcase Example:  '[2,5]\n[[3,0,5],[1,2,10]]\n[3,2]'
#
# 
# In LeetCode Store, there are some kinds of items to sell. Each item has a
# price.
# 
# 
# 
# However, there are some special offers, and a special offer consists of one
# or more different kinds of items with a sale price.
# 
# 
# 
# You are given the each item's price, a set of special offers, and the number
# we need to buy for each item.
# The job is to output the lowest price you have to pay for exactly certain
# items as given, where you could make optimal use of the special offers.
# 
# 
# 
# Each special offer is represented in the form of an array, the last number
# represents the price you need to pay for this special offer, other numbers
# represents how many specific items you could get if you buy this offer.
# 
# 
# You could use any of special offers as many times as you want.
# 
# Example 1:
# 
# Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
# Output: 14
# Explanation: 
# There are two kinds of items, A and B. Their prices are $2 and $5
# respectively. 
# In special offer 1, you can pay $5 for 3A and 0B
# In special offer 2, you can pay $10 for 1A and 2B. 
# You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer
# #2), and $4 for 2A.
# 
# 
# 
# Example 2:
# 
# Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
# Output: 11
# Explanation: 
# The price of A is $2, and $3 for B, $4 for C. 
# You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
# You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer
# #1), and $3 for 1B, $4 for 1C. 
# You cannot add more items, though only $9 for 2A ,2B and 1C.
# 
# 
# 
# Note:
# 
# There are at most 6 kinds of items, 100 special offers.
# For each item, you need to buy at most 6 of them.
# You are not allowed to buy more items than you want, even if that would lower
# the overall price.
# 
# 
#
from collections import defaultdict
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        dp = {}
        def traverse(needs):
            if not max(needs):
                return 0
            if tuple(needs) in dp:
                return dp[tuple(needs)] 
            ret = sum(needs[i] * p for i, p in enumerate(price))
            for i, sp in enumerate(special):
                if all(needs[item] >= cnt for item, cnt in enumerate(sp[:-1])):
                    for item, cnt in enumerate(sp[:-1]):
                        needs[item] -= cnt
                    ret = min(ret, sp[-1] + traverse(needs))
                    for item, cnt in enumerate(sp[:-1]):
                        needs[item] += cnt
            dp[tuple(needs)] = ret
            return ret
        ret = traverse(needs)
        return ret

    def test(self):
        #print self.shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1])
        #print self.shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2])
        print self.shoppingOffers([9,6,1,5,3,4], [[1,2,2,1,0,4,14],[6,3,4,0,0,1,16],[4,5,6,6,2,4,26],[1,1,4,3,4,3,15],[4,2,5,4,4,5,15],[4,0,0,2,3,5,13],[2,4,6,4,3,5,7],[3,3,4,2,2,6,21],[0,3,0,2,3,3,15],[0,2,4,2,2,5,24],[4,1,5,4,5,4,25],[6,0,5,0,1,1,14],[4,0,5,2,1,5,8],[4,1,4,4,3,1,10],[4,4,2,1,5,0,14],[2,4,4,1,3,1,16],[4,2,3,1,2,1,26],[2,4,1,6,5,3,2],[0,2,0,4,0,0,19],[3,1,6,3,3,1,23],[6,2,3,2,4,4,16],[5,3,5,5,0,4,5],[5,0,4,3,0,2,20],[5,3,1,2,2,5,8],[3,0,6,1,0,2,10],[5,6,6,1,0,4,12],[0,6,6,4,6,4,21],[0,4,6,5,0,0,22],[0,4,2,4,4,6,16],[4,2,1,0,6,5,14],[0,1,3,5,0,3,8],[5,5,3,3,2,0,4],[1,0,3,6,2,3,18],[4,2,6,2,2,5,2],[0,2,5,5,3,6,12],[1,0,6,6,5,0,10],[6,0,0,5,5,1,24],[1,4,6,5,6,3,19],[2,2,4,2,4,2,20],[5,6,1,4,0,5,3],[3,3,2,2,1,0,14],[0,1,3,6,5,0,9],[5,3,6,5,3,3,11],[5,3,3,1,0,2,26],[0,1,1,4,2,1,16],[4,2,3,2,1,4,6],[0,2,1,3,3,5,15],[5,6,4,1,2,5,18],[1,0,0,1,6,1,16],[2,0,6,6,2,2,17],[4,4,0,2,4,6,12],[0,5,2,5,4,6,6],[5,2,1,6,2,1,24],[2,0,2,2,0,1,14],[1,1,0,5,3,5,16],[0,2,3,5,5,5,6],[3,2,0,6,4,6,8],[4,0,1,4,5,1,6],[5,0,5,6,6,3,7],[2,6,0,0,2,1,25],[0,4,6,1,4,4,6],[6,3,1,4,1,1,24],[6,2,1,2,1,4,4],[0,1,2,3,0,1,3],[0,2,5,6,5,2,13],[2,6,4,2,2,3,17],[3,4,5,0,5,4,20],[6,2,3,4,1,3,4],[6,4,0,0,0,5,16],[3,1,2,5,0,6,11],[1,3,2,2,5,6,14],[1,3,4,5,3,5,18],[2,1,1,2,6,1,1],[4,0,4,0,6,6,8],[4,6,0,5,0,2,1],[3,1,0,5,3,2,26],[4,0,4,0,6,6,6],[5,0,0,0,0,4,26],[4,3,2,2,0,2,14],[5,2,4,0,2,2,26],[3,4,6,0,2,4,25],[2,1,5,5,1,3,26],[0,5,2,4,0,2,24],[5,2,5,4,5,0,1],[5,3,0,1,5,4,15],[6,1,5,1,2,1,21],[2,5,1,2,1,4,15],[1,4,4,0,0,0,1],[5,0,6,1,1,4,22],[0,1,1,6,1,4,1],[1,6,0,3,2,2,17],[3,4,3,3,1,5,17],[1,5,5,4,5,2,27],[0,6,5,5,0,0,26],[1,4,0,3,1,0,13],[1,0,3,5,2,4,5],[2,2,2,3,0,0,11],[3,2,2,1,1,1,6],[6,6,1,1,1,6,26],[1,5,1,2,5,2,12]], [6,6,6,1,6,6])
