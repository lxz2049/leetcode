#
# [815] Champagne Tower
#
# https://leetcode.com/problems/champagne-tower/description/
#
# algorithms
# Medium (30.44%)
# Total Accepted:    5K
# Total Submissions: 16.2K
# Testcase Example:  '1\n1\n1'
#
# We stack glasses in a pyramid, where the first row has 1 glass, the second
# row has 2 glasses, and so on until the 100th row.  Each glass holds one cup
# (250ml) of champagne.
# 
# Then, some champagne is poured in the first glass at the top.  When the top
# most glass is full, any excess liquid poured will fall equally to the glass
# immediately to the left and right of it.  When those glasses become full, any
# excess champagne will fall equally to the left and right of those glasses,
# and so on.  (A glass at the bottom row has it's excess champagne fall on the
# floor.)
# 
# For example, after one cup of champagne is poured, the top most glass is
# full.  After two cups of champagne are poured, the two glasses on the second
# row are half full.  After three cups of champagne are poured, those two cups
# become full - there are 3 full glasses total now.  After four cups of
# champagne are poured, the third row has the middle glass half full, and the
# two outside glasses are a quarter full, as pictured below.
# 
# 
# 
# Now after pouring some non-negative integer cups of champagne, return how
# full the j-th glass in the i-th row is (both i and j are 0 indexed.)
# 
# 
# 
# 
# Example 1:
# Input: poured = 1, query_glass = 1, query_row = 1
# Output: 0.0
# Explanation: We poured 1 cup of champange to the top glass of the tower
# (which is indexed as (0, 0)). There will be no excess liquid so all the
# glasses under the top glass will remain empty.
# 
# Example 2:
# Input: poured = 2, query_glass = 1, query_row = 1
# Output: 0.5
# Explanation: We poured 2 cups of champange to the top glass of the tower
# (which is indexed as (0, 0)). There is one cup of excess liquid. The glass
# indexed as (1, 0) and the glass indexed as (1, 1) will share the excess
# liquid equally, and each will get half cup of champange.
# 
# 
# 
# 
# Note:
# 
# 
# poured will be in the range of [0, 10 ^ 9].
# query_glass and query_row will be in the range of [0, 99].
# 
# 
# 
# 
#
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        tower = [[poured]]
        for row in xrange(1, query_row+1):
            tower.append([0] * (row + 1))
            for glass in xrange(row+1):
                left = right = 0
                if glass > 0 and tower[row-1][glass-1] > 1:
                    left = (tower[row-1][glass-1] - 1) / 2.0 
                if glass < row and tower[row-1][glass] > 1:
                    right = (tower[row-1][glass] - 1) / 2.0
                tower[row][glass] = left + right
                if query_row == row and query_glass == glass:
                    break
        return min(1, tower[query_row][query_glass])

    def test(self):
        print self.champagneTower(2, 1, 1)
        print self.champagneTower(0, 1, 1)
        print self.champagneTower(1, 1, 1)
        print self.champagneTower(2, 1, 0)
        print self.champagneTower(2, 1, 1)
