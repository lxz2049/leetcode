#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (34.97%)
# Total Accepted:    72.6K
# Total Submissions: 207.4K
# Testcase Example:  '5\n7'
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
# of all numbers in this range, inclusive.
# 
# Example 1:
# 
# 
# Input: [5,7]
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: [0,1]
# Output: 0
#
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        for b in xrange(32):
            mask = (1 << b)
            #print m & mask, (m & (0xffffffff << b)) + mask
            if m & mask and n >= (m & (0xffffffff << b)) + mask:
                m ^= mask
        return m

    def test(self):
        print self.rangeBitwiseAnd(5, 7)
        print self.rangeBitwiseAnd(0, 1)

