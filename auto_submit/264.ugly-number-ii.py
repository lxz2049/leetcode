#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (34.62%)
# Total Accepted:    90.3K
# Total Submissions: 259.8K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# Note:  
# 
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
#
import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = [1]
        two = three = five = 0
        for _ in xrange(1, n):
            next_two = ret[two] * 2
            next_three = ret[three] * 3
            next_five = ret[five] * 5
            ret.append(min(next_two, next_three, next_five))
            if ret[-1] == next_two:
                two += 1
            if ret[-1] == next_three:
                three += 1
            if ret[-1] == next_five:
                five += 1
        return ret[-1]

    def test(self):
        for i in xrange(50):
            print self.nthUglyNumber(i)
        print self.nthUglyNumber(1680)
