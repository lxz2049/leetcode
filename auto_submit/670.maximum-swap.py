#
# [670] Maximum Swap
#
# https://leetcode.com/problems/maximum-swap/description/
#
# algorithms
# Medium (38.82%)
# Total Accepted:    29.5K
# Total Submissions: 75.9K
# Testcase Example:  '2736'
#
# 
# Given a non-negative integer, you could swap two digits at most once to get
# the maximum valued number. Return the maximum valued number you could get.
# 
# 
# Example 1:
# 
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# 
# 
# 
# Example 2:
# 
# Input: 9973
# Output: 9973
# Explanation: No swap.
# 
# 
# 
# 
# Note:
# 
# The given number is in the range [0, 108]
# 
# 
#
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        numstr = str(num)
        for i, n in enumerate(numstr):
            if i and n > numstr[i-1]:
                i = max(((numstr[i], i) for i in xrange(i, len(numstr))))[1]
                j = next(j for j in xrange(i) if numstr[i] > numstr[j])
                ret = numstr[:j] + numstr[i] + numstr[j+1:i] + numstr[j] + numstr[i+1:]
                return int(ret)
        return num

    def test(self):
        print self.maximumSwap(9973)
        print self.maximumSwap(22236)
        print self.maximumSwap(98368)
        print self.maximumSwap(43456)
