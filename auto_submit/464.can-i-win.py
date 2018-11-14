#
# [464] Can I Win
#
# https://leetcode.com/problems/can-i-win/description/
#
# algorithms
# Medium (26.23%)
# Total Accepted:    28.7K
# Total Submissions: 109.4K
# Testcase Example:  '10\n11'
#
# In the "100 game," two players take turns adding, to a running total, any
# integer from 1..10. The player who first causes the running total to reach or
# exceed 100 wins. 
# 
# What if we change the game so that players cannot re-use integers? 
# 
# For example, two players might take turns drawing from a common pool of
# numbers of 1..15 without replacement until they reach a total >= 100.
# 
# Given an integer maxChoosableInteger and another integer desiredTotal,
# determine if the first player to move can force a win, assuming both players
# play optimally. 
# 
# You can always assume that maxChoosableInteger will not be larger than 20 and
# desiredTotal will not be larger than 300.
# 
# 
# Example
# 
# Input:
# maxChoosableInteger = 10
# desiredTotal = 11
# 
# Output:
# false
# 
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from
# 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >=
# desiredTotal.
# Same with other integers chosen by the first player, the second player will
# always win.
# 
# 
#
class Solution(object):
    def canIWin(self, m, target):
        if (m + 1) * m / 2 < target:
            return False
        if m and not target:
            return True
        dp = {}
        def traverse(total, mask):
            if total >= target:
                return False
            if mask in dp:
                return dp[mask]
            for i in xrange(m):
                b = 1 << i
                if not mask & b and not traverse(total+i+1, mask | b):
                    dp[mask] = True
                    return dp[mask]
            dp[mask] = False
            return dp[mask]
        ret = traverse(0, 0)
        return ret

    def test(self):
        print self.canIWin(10, 11)
        print self.canIWin(10, 0)
