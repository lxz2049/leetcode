#
# [799] Minimum Distance Between BST Nodes
#
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (48.72%)
# Total Accepted:    20.8K
# Total Submissions: 42.7K
# Testcase Example:  '[4,2,6,1,3,null,null]'
#
# Given a Binary Search Tree (BST) with the root node root, return the minimum
# difference between the values of any two different nodes in the tree.
# 
# Example :
# 
# 
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.
# 
# The given tree [4,2,6,1,3,null,null] is represented by the following
# diagram:
# 
# ⁠         4
# ⁠       /   \
# ⁠     2      6
# ⁠    / \    
# ⁠   1   3  
# 
# while the minimum difference in this tree is 1, it occurs between node 1 and
# node 2, also between node 3 and node 2.
# 
# 
# Note:
# 
# 
# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's
# value is different.
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
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0x7fffffff
        self.last = None
        def traverse(node):
            if node:
                traverse(node.left)
                if self.last is not None:
                    self.ret = min(self.ret, node.val - self.last)
                self.last = node.val
                traverse(node.right)
        traverse(root)
        return self.ret

