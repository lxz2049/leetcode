#
# [971] Shortest Bridge
#
# https://leetcode.com/problems/shortest-bridge/description/
#
# algorithms
# Medium (41.57%)
# Total Accepted:    3.1K
# Total Submissions: 7.4K
# Testcase Example:  '[[0,1],[1,0]]'
#
# In a given 2D binary array A, there are two islands.  (An island is a
# 4-directionally connected group of 1s not connected to any other 1s.)
# 
# Now, we may change 0s to 1s so as to connect the two islands together to form
# 1 island.
# 
# Return the smallest number of 0s that must be flipped.  (It is guaranteed
# that the answer is at least 1.)
# 
# 
# 
# Example 1:
# 
# 
# Input: [[0,1],[1,0]]
# Output: 1
# 
# 
# 
# Example 2:
# 
# 
# Input: [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# 
# 
# 
# Example 3:
# 
# 
# Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length = A[0].length <= 100
# A[i][j] == 0 or A[i][j] == 1
# 
# 
# 
# 
# 
# 
# 
#
from collections import deque
class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        graph = [[0 for _ in A[0]] for _ in A]
        island = deque([])
        def traverse(x, y):
            graph[x][y] = 1
            island.append((x, y))
            for i, j in ((x, y+1), (x+1, y), (x, y-1), (x-1, y)):
                if i >= 0 and i < len(A) and j >= 0 and j < len(A[0]):
                    if not graph[i][j] and A[i][j] == 1:
                        traverse(i, j)
                        
        for i in xrange(len(A)):
            for j in xrange(len(A[i])):
                if A[i][j]:
                    traverse(i, j)
                    while island:
                        x, y = island.pop()
                        dist = graph[x][y]
                        for i, j in ((x, y+1), (x+1, y), (x, y-1), (x-1, y)):
                            if i >= 0 and i < len(A) and j >= 0 and j < len(A[0]):
                                if not graph[i][j]:
                                    if A[i][j] == 1:
                                        return dist - 1
                                    graph[i][j] = dist + 1
                                    island.appendleft((i, j))
        return -1

    def test(self):
        print self.shortestBridge([[0,1],[1,0]])
        print self.shortestBridge([[0,1,0],[0,0,0],[0,0,1]])
        print self.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]])
