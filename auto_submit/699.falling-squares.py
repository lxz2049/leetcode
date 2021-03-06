#
# [699] Falling Squares
#
# https://leetcode.com/problems/falling-squares/description/
#
# algorithms
# Hard (38.51%)
# Total Accepted:    6.8K
# Total Submissions: 17.7K
# Testcase Example:  '[[1,2],[2,3],[6,1]]'
#
# On an infinite number line (x-axis), we drop given squares in the order they
# are given.
# The i-th square dropped (positions[i] = (left, side_length)) is a square with
# the left-most point being positions[i][0] and sidelength positions[i][1].
# The square is dropped with the bottom edge parallel to the number line, and
# from a higher height than all currently landed squares.  We wait for each
# square to stick before dropping the next.
# The squares are infinitely sticky on their bottom edge, and will remain fixed
# to any positive length surface they touch (either the number line or another
# square).  Squares dropped adjacent to each other will not stick together
# prematurely.
# 
# 
# Return a list ans of heights.  Each height ans[i] represents the current
# highest height of any square we have dropped, after dropping squares
# represented by positions[0], positions[1], ..., positions[i].
# 
# 
# Example 1:
# 
# Input: [[1, 2], [2, 3], [6, 1]]
# Output: [2, 5, 5]
# Explanation:
# 
# After the first drop of positions[0] = [1, 2]:
# _aa
# _aa
# -------
# The maximum height of any square is 2.
# 
# After the second drop of positions[1] = [2, 3]:
# __aaa
# __aaa
# __aaa
# _aa__
# _aa__
# --------------
# The maximum height of any square is 5.  
# The larger square stays on top of the smaller square despite where its center
# of gravity is, because squares are infinitely sticky on their bottom edge.
# 
# After the third drop of positions[1] = [6, 1]:
# __aaa
# __aaa
# __aaa
# _aa
# _aa___a
# --------------
# The maximum height of any square is still 5.
# 
# Thus, we return an answer of [2, 5, 5].
# 
# 
# 
# 
# 
# Example 2:
# 
# Input: [[100, 100], [200, 100]]
# Output: [100, 100]
# Explanation: Adjacent squares don't get stuck prematurely - only their bottom
# edge can stick to surfaces.
# 
# 
# 
# Note:
# 1 .
# 1 .
# 1 .
# 
#
class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ret = [0 for _ in positions]
        heights = [h for _, h in positions]
        for i, rect in enumerate(positions):
            for j, bottom in enumerate(positions[:i]):
                if rect[0] + rect[1] > bottom[0] and \
                   bottom[0] + bottom[1] > rect[0]:
                       heights[i] = max(heights[i], heights[j] + rect[1])
            ret[i] = max(ret[i-1], heights[i])
        return ret

    def test(self):
        #print self.fallingSquares( [[1, 2], [2, 3], [6, 1]])
        #print self.fallingSquares([[100, 100], [200, 100]])
        print self.fallingSquares( [[2, 1], [2, 9], [1, 8]])
