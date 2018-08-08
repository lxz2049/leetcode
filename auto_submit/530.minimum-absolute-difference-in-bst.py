#
# [530] Minimum Absolute Difference in BST
#
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (47.30%)
# Total Accepted:    41.9K
# Total Submissions: 87.1K
# Testcase Example:  '[1,null,3,2]'
#
# Given a binary search tree with non-negative values, find the minimum
# absolute difference between values of any two nodes.
# 
# 
# Example:
# 
# Input:
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
# 
# Output:
# 1
# 
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1
# (or between 2 and 3).
# 
# 
# 
# 
# Note:
# There are at least two nodes in this BST.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min_diff = 0xffffffff
        def traverse(prev_val, node):
            if node.left:
                prev_val = traverse(prev_val, node.left)
            if prev_val is not None:
                self.min_diff = min(self.min_diff, abs(prev_val - node.val))
            prev_val = node.val
            if node.right:
                prev_val = traverse(prev_val, node.right)
            return prev_val
        traverse(None, root)
        return self.min_diff

