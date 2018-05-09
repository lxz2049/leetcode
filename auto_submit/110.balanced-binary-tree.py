#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (38.38%)
# Total Accepted:    226.7K
# Total Submissions: 588.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the depth of the two subtrees of every node never
# differ by more than 1.
# 
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# Return false.
# 
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.height1 = self.height2 = None
        def traverse(node):
            if node:
                balanced_left, height_left = traverse(node.left) 
                balanced_right, height_right = traverse(node.right)
                #print node.val, balanced_left, height_left, balanced_right, height_right
                balanced = balanced_left and balanced_right and abs(height_left - height_right) <= 1
                height = max(height_left, height_right) + 1
                return balanced, height
            return True, 0
        return traverse(root)[0]

    def test(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)
        root.left.right.left = TreeNode(4)
        root.left.right.right = TreeNode(4)
        root.right.left.left = TreeNode(4)
        root.right.left.right = TreeNode(4)
        #root.right.right.left = TreeNode(4)
        #root.right.right.right = TreeNode(4)
        root.left.left.left.left = TreeNode(5)
        root.left.left.left.right = TreeNode(5)


        print self.isBalanced(root)
