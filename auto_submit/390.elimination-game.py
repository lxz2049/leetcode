#
# [390] Elimination Game
#
# https://leetcode.com/problems/elimination-game/description/
#
# algorithms
# Medium (42.62%)
# Total Accepted:    16.7K
# Total Submissions: 39.3K
# Testcase Example:  '9'
#
# 
# There is a list of sorted integers from 1 to n. Starting from left to right,
# remove the first number and every other number afterward until you reach the
# end of the list.
# 
# Repeat the previous step again, but this time from right to left, remove the
# right most number and every other number from the remaining numbers.
# 
# We keep repeating the steps again, alternating left to right and right to
# left, until a single number remains.
# 
# Find the last number that remains starting with a list of length n.
# 
# Example:
# 
# Input:
# n = 9,
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8
# 2 6
# 6
# 
# Output:
# 6
# 
# 
#
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        step = 1
        while start != end:
            cnt = (start-end) / step + 1
            #print start, end, cnt
            start, end = end - (cnt%2) * step, start + step
            step *= -2
        return start

    def test(self):
        print self.lastRemaining(4)
        print self.lastRemaining(9)
