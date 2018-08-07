#
# [501] Find Mode in Binary Search Tree
#
# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (37.57%)
# Total Accepted:    39.4K
# Total Submissions: 103.9K
# Testcase Example:  '[1,null,2,2]'
#
# Given a binary search tree (BST) with duplicates, find all the mode(s) (the
# most frequently occurred element) in the given BST.
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than or equal
# to the node's key.
# The right subtree of a node contains only nodes with keys greater than or
# equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# 
# For example:
# Given BST [1,null,2,2],
# 
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  2
# 
# 
# 
# 
# return [2].
# 
# Note: If a tree has more than one mode, you can return them in any order.
# 
# Follow up: Could you do that without using any extra space? (Assume that the
# implicit stack space incurred due to recursion does not count).
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ret = []
        self.mode_cnt = 0
        def update_mode(val, cnt):
            if cnt > self.mode_cnt:
                self.ret = [val]
                self.mode_cnt = cnt
            elif cnt == self.mode_cnt:
                self.ret.append(val)

        def traverse(val, cnt, node):
            if node.left:
                val, cnt = traverse(val, cnt, node.left)
            if val == node.val:
                cnt += 1
            else:
                val = node.val
                cnt = 1
            update_mode(val, cnt)
            if node.right:
                val, cnt = traverse(val, cnt, node.right)
            return val, cnt

        if root:
            traverse(None, 0, root)
        return self.ret

    def test(self):
        print self.findMode()
