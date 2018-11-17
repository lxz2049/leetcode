#
# [930] All Possible Full Binary Trees
#
# https://leetcode.com/problems/all-possible-full-binary-trees/description/
#
# algorithms
# Medium (65.87%)
# Total Accepted:    7.9K
# Total Submissions: 11.9K
# Testcase Example:  '7'
#
# A full binary tree is a binary tree where each node has exactly 0 or 2
# children.
# 
# Return a list of all possible full binary trees with N nodes.  Each element
# of the answer is the root node of one possible tree.
# 
# Each node of each tree in the answer must have node.val = 0.
# 
# You may return the final list of trees in any order.
# 
# 
# 
# Example 1:
# 
# 
# Input: 7
# Output:
# [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 20
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution(object):
    memo = {0: [], 1: [TreeNode(0)]}
    def allPossibleFBT(self, N):
        if N not in Solution.memo:
            Solution.memo[N] = []
            for l in xrange(1, N, 2):
                r = N - 1 - l
                for left in self.allPossibleFBT(l):
                    for right in self.allPossibleFBT(r):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        Solution.memo[N].append(root)
        return Solution.memo[N]
    
    def test(self):
        print self.allPossibleFBT(7)

