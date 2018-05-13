#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (38.15%)
# Total Accepted:    146.7K
# Total Submissions: 381.4K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the kth index row of the
# Pascal's triangle.
# 
# Note that the row index starts from 0.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 3
# Output: [1,3,3,1]
# 
# 
# Follow up:
# 
# Could you optimize your algorithm to use only O(k) extra space?
# 
#
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [1]
        for i in range(0, rowIndex):
            ret = [(ret[j-1] if j > 0 else 0) + (ret[j] if j < len(ret) else 0) 
                    for j in range(0, len(ret)+1)]
        return ret

    def test(self):
        print self.getRow(3)
        print self.getRow(4)
        print self.getRow(5)
