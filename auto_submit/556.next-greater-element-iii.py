#
# [556] Next Greater Element III
#
# https://leetcode.com/problems/next-greater-element-iii/description/
#
# algorithms
# Medium (29.00%)
# Total Accepted:    18.6K
# Total Submissions: 64.2K
# Testcase Example:  '12'
#
# Given a positive 32-bit integer n, you need to find the smallest 32-bit
# integer which has exactly the same digits existing in the integer n and is
# greater in value than n. If no such positive 32-bit integer exists, you need
# to return -1.
# 
# Example 1:
# 
# 
# Input: 12
# Output: 21
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 21
# Output: -1
# 
# 
# 
# 
#
class Solution(object):
    def nextGreaterElement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(reversed(str(num)))
        for i in xrange(1, len(num)):
            if num[i-1] > num[i]:
                j = next(j for j in xrange(i) if num[j] > num[i])
                num[i], num[j] = num[j], num[i]
                ret = num[:i][::-1] + num[i:]
                ret = ret[::-1]
                ret = int("".join(ret))
                if ret <= 0x7fffffff:
                    return ret
        return -1

    def test(self):
        print self.nextGreaterElement(1243)
        print self.nextGreaterElement(230241)
        print self.nextGreaterElement(12)
        print self.nextGreaterElement(21)
        print self.nextGreaterElement(1999999999)
