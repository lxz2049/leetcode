#
# [400] Nth Digit
#
# https://leetcode.com/problems/nth-digit/description/
#
# algorithms
# Easy (30.14%)
# Total Accepted:    34.8K
# Total Submissions: 115.7K
# Testcase Example:  '3'
#
# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8,
# 9, 10, 11, ... 
# 
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n <
# 231).
# 
# 
# Example 1:
# 
# Input:
# 3
# 
# Output:
# 3
# 
# 
# 
# Example 2:
# 
# Input:
# 11
# 
# Output:
# 0
# 
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
# which is part of the number 10.
# 
# 
#
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit_len = 1
        digit_range = 9
        digit_start = 1
        n -= 1
        while n:
            if n < digit_range * digit_len:
                break
            n -= digit_range * digit_len
            digit_start += digit_range
            digit_len += 1
            digit_range *= 10
        digit = digit_start + n / digit_len 
        digit_pos = n % digit_len
        #print "n", n, "len", digit_len, "range", digit_range, "start", digit_start, "digit", digit, "pos", digit_pos
        return int(str(digit)[digit_pos])

    def test(self):
        print self.findNthDigit(3)
        print self.findNthDigit(9)
        print self.findNthDigit(11)
        print self.findNthDigit(30)
        print self.findNthDigit(300)
            
