#
# [623] Add One Row to Tree
#
# https://leetcode.com/problems/add-one-row-to-tree/description/
#
# algorithms
# Medium (46.12%)
# Total Accepted:    18.5K
# Total Submissions: 40.2K
# Testcase Example:  '[4,2,6,3,1,5]\n1\n2'
#
# Given the root of a binary tree, then value v and depth d, you need to add a
# row of nodes with value v at the given depth d. The root node is at depth
# 1. 
# 
# The adding rule is: given a positive integer depth d, for each NOT null tree
# nodes N in depth d-1, create two tree nodes with value v as N's left subtree
# root and right subtree root. And N's original left subtree should be the left
# subtree of the new left subtree root, its original right subtree should be
# the right subtree of the new right subtree root. If depth d is 1 that means
# there is no depth d-1 at all, then create a tree node with value v as the new
# root of the whole original tree, and the original tree is the new root's left
# subtree.
# 
# Example 1:
# 
# Input: 
# A binary tree as following:
# ⁠      4
# ⁠    /   \
# ⁠   2     6
# ⁠  / \   / 
# ⁠ 3   1 5   
# 
# v = 1
# 
# d = 2
# 
# Output: 
# ⁠      4
# ⁠     / \
# ⁠    1   1
# ⁠   /     \
# ⁠  2       6
# ⁠ / \     / 
# ⁠3   1   5   
# 
# 
# 
# 
# 
# Example 2:
# 
# Input: 
# A binary tree as following:
# ⁠     4
# ⁠    /   
# ⁠   2    
# ⁠  / \   
# ⁠ 3   1    
# 
# v = 1
# 
# d = 3
# 
# Output: 
# ⁠     4
# ⁠    /   
# ⁠   2
# ⁠  / \    
# ⁠ 1   1
# ⁠/     \  
# 3       1
# 
# 
# 
# Note:
# 
# The given d is in range [1, maximum depth of the given tree + 1].
# The given binary tree has at least one tree node.
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
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root 
            return new_root

        def traverse(node, depth, target):
            if not node:
                return
            if depth == target - 1:
                new_left = TreeNode(v)
                node.left, new_left.left = new_left, node.left
                new_right = TreeNode(v)
                node.right, new_right.right = new_right, node.right
            else:
                traverse(node.left, depth + 1, target)
                traverse(node.right, depth + 1, target)
        traverse(root, 1, d)
        return root