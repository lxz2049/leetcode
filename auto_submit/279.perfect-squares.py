#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (37.72%)
# Total Accepted:    101.3K
# Total Submissions: 268.6K
# Testcase Example:  '1'
#
# 
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# 
# 
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13,
# return 2 because 13 = 4 + 9.
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = int(math.sqrt(n))
        dp = [0x7fffffff] * (n + 1)
        dp[0] = 0
        for i in xrange(1, count+1):
            for j in xrange(i*i, n+1):
                dp[j] = min(dp[j], dp[j-i*i] + 1)
        return dp[n]

"""
if __name__ == "__main__":
    print 1, Solution().numSquares(1)
    print 12, Solution().numSquares(12)
    print 13, Solution().numSquares(13)
    print 112, Solution().numSquares(112)
    """
