#
# [483] Smallest Good Base
#
# https://leetcode.com/problems/smallest-good-base/description/
#
# algorithms
# Hard (33.68%)
# Total Accepted:    8.4K
# Total Submissions: 24.9K
# Testcase Example:  '"13"'
#
# For an integer n, we call k>=2 a good base of n, if all digits of n base k
# are 1.
# Now given a string representing n, you should return the smallest good base
# of n in string format. 
# 
# Example 1:
# 
# Input: "13"
# Output: "3"
# Explanation: 13 base 3 is 111.
# 
# 
# 
# Example 2:
# 
# Input: "4681"
# Output: "8"
# Explanation: 4681 base 8 is 11111.
# 
# 
# 
# Example 3:
# 
# Input: "1000000000000000000"
# Output: "999999999999999999"
# Explanation: 1000000000000000000 base 999999999999999999 is 11.
# 
# 
# 
# Note:
# 
# The range of n is [3, 10^18].
# The string representing n is always valid and will not have leading zeros.
# 
# 
#
class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)
        def calc(bitCount, base):
            ret = 0
            carry = 1
            for i in xrange(bitCount):
                ret += carry
                carry *= base
            return ret

        for bitCount in xrange(60, 1, -1):
            lo = 2
            hi = n-1
            while lo <= hi:
                mid = (lo + hi) / 2
                m = calc(bitCount, mid)
                if m == n:
                    return str(mid)
                if m < n:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return "-1"

    def test(self):
        print self.smallestGoodBase(13)
        print self.smallestGoodBase(4681)
        print self.smallestGoodBase(1000000000000000000)
