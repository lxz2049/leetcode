#
# [984] Most Stones Removed with Same Row or Column
#
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
#
# algorithms
# Medium (49.28%)
# Total Accepted:    6.4K
# Total Submissions: 12.4K
# Testcase Example:  '[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]'
#
# On a 2D plane, we place stones at some integer coordinate points.  Each
# coordinate point may have at most one stone.
# 
# Now, a move consists of removing a stone that shares a column or row with
# another stone on the grid.
# 
# What is the largest possible number of moves we can make?
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# 
# 
# 
# Example 2:
# 
# 
# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# 
# 
# 
# Example 3:
# 
# 
# Input: stones = [[0,0]]
# Output: 0
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= stones.length <= 1000
# 0 <= stones[i][j] < 10000
# 
# 
# 
# 
# 
#
from collections import defaultdict
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        parents = range(len(stones))
        size = [1] * len(stones)
        def find(a):
            if parents[a] != a:
                parents[a] = find(parents[a])
            return parents[a]

        def merge(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return
            if size[a] < size[b]:
                a, b = b, a
            parents[b] = a
            size[a] += size[b]

        cols = defaultdict(list)
        rows = defaultdict(list)
        for i, s in enumerate(stones):
           col, row = s
           if cols[col]:
               merge(i, cols[col][0])
           if rows[row]:
               merge(i, rows[row][0])
           cols[col].append(i)
           rows[row].append(i)

        return len(stones) - len(set([find(p) for p in parents]))

    def test(self):
        print self.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])
        print self.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]])
        print self.removeStones([[0,0]])
