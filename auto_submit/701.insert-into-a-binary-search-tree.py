#
# [784] Insert into a Binary Search Tree
#
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
#
# algorithms
# Medium (64.88%)
# Total Accepted:    9.7K
# Total Submissions: 15K
# Testcase Example:  '[4,2,7,1,3]\n5'
#
# Given the root node of a binary search tree (BST) and a value to be inserted
# into the tree, insert the value into the BST. Return the root node of the BST
# after the insertion. It is guaranteed that the new value does not exist in
# the original BST.
# 
# Note that there may exist multiple valid ways for the insertion, as long as
# the tree remains a BST after insertion. You can return any of them.
# 
# For example, 
# 
# 
# Given the tree:
# ⁠       4
# ⁠      / \
# ⁠     2   7
# ⁠    / \
# ⁠   1   3
# And the value to insert: 5
# 
# 
# You can return this binary search tree:
# 
# 
# ⁠        4
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   /
# ⁠   1   3 5
# 
# 
# This tree is also valid:
# 
# 
# ⁠        5
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   
# ⁠   1   3
# ⁠        \
# ⁠         4
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def traverse(node, val):
            if not node:
                return TreeNode(val)
            else:
                if val > node.val:
                    node.right = traverse(node.right, val)
                else:
                    node.left = traverse(node.left, val)
            return node

        return traverse(root, val)
