#
# @lc app=leetcode id=111 lang=python
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (35.05%)
# Total Accepted:    295.3K
# Total Submissions: 836.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its minimum depth = 2.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = deque([(root, 1)])
        while q:
            node, depth = q.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
        return 0
