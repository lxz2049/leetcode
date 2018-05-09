#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (39.83%)
# Total Accepted:    165.4K
# Total Submissions: 414.4K
# Testcase Example:  '0'
#
# Given numRows, generate the first numRows of Pascal's triangle.
# 
# 
# For example, given numRows = 5,
# Return
# 
# [
# [1],
# [1,1],
# [1,2,1],
# [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        ret = [[1]]
        for i in range(1, numRows):
            #print [(j-1, j) for j in range(0, i+1)]
            row = [(ret[i-1][j-1] if j > 0 else 0) + (ret[i-1][j] if j < i else 0) for j in range(0, i+1)]
            ret.append(row)
        return ret

    def test(self):
        print self.generate(5)
            
