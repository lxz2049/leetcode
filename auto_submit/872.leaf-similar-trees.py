#
# [904] Leaf-Similar Trees
#
# https://leetcode.com/problems/leaf-similar-trees/description/
#
# algorithms
# Easy (60.97%)
# Total Accepted:    16.2K
# Total Submissions: 26.6K
# Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
#
# Consider all the leaves of a binary tree.  From left to right order, the
# values of those leaves form a leaf value sequence.
# 
# 
# 
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
# 8).
# 
# Two binary trees are considered leaf-similar if their leaf value sequence is
# the same.
# 
# Return true if and only if the two given trees with head nodes root1 and
# root2 are leaf-similar.
# 
# 
# 
# Note:
# 
# 
# Both of the given trees will have between 1 and 100 nodes.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from itertools import izip_longest
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def traverse(root):
            if not root:
                return
            for leaf in traverse(root.left):
                yield leaf
            for leaf in traverse(root.right):
                yield leaf
            if not root.left and not root.right:
                yield root.val

        return all(a == b for a, b in izip_longest(traverse(root1), traverse(root2)))
