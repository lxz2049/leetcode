#
# [738] Monotone Increasing Digits
#
# https://leetcode.com/problems/monotone-increasing-digits/description/
#
# algorithms
# Medium (41.31%)
# Total Accepted:    10K
# Total Submissions: 24.4K
# Testcase Example:  '10'
#
# 
# Given a non-negative integer N, find the largest number that is less than or
# equal to N with monotone increasing digits.
# 
# (Recall that an integer has monotone increasing digits if and only if each
# pair of adjacent digits x and y satisfy x .)
# 
# 
# Example 1:
# 
# Input: N = 10
# Output: 9
# 
# 
# 
# Example 2:
# 
# Input: N = 1234
# Output: 1234
# 
# 
# 
# Example 3:
# 
# Input: N = 332
# Output: 299
# 
# 
# 
# Note:
# N is an integer in the range [0, 10^9].
# 
#
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        num = str(N)
        idx = None
        min_num = '9'
        for i in xrange(len(num) - 1, -1, -1):
            n = num[i]
            min_num = min(n, min_num)
            if n > min_num:
                idx = i
                N = num[:idx] + str(int(n)-1) + "9" * (len(num) - 1 - idx)
                return self.monotoneIncreasingDigits(int(N))
        return N

    def test(self):
        print self.monotoneIncreasingDigits(0)
        print self.monotoneIncreasingDigits(101)
        print self.monotoneIncreasingDigits(10)
        print self.monotoneIncreasingDigits(1234)
        print self.monotoneIncreasingDigits(332)
        print self.monotoneIncreasingDigits(120)
