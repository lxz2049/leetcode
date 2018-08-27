#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (40.18%)
# Total Accepted:    61K
# Total Submissions: 151.1K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# 
# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a
# tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
# 
# 
# Example 1:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# 
# Given tree t:
# 
# ⁠  4 
# ⁠ / \
# ⁠1   2
# 
# Return true, because t has the same structure and node values with a subtree
# of s.
# 
# 
# Example 2:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
# 
# Given tree t:
# 
# ⁠  4
# ⁠ / \
# ⁠1   2
# 
# Return false.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSubtreeRecursive(node_s, node_t):
            if not node_s and not node_t:
                return True
            #print "issub", node_s.val if node_s else "", node_t.val if node_t else ""
            if node_s and node_t and node_s.val == node_t.val:
                return isSubtreeRecursive(node_s.left, node_t.left) and \
                       isSubtreeRecursive(node_s.right, node_t.right)
            return False

        def traverse(node):
            if not node:
                return False
            #print "traverse", node.val
            match = isSubtreeRecursive(node, t)
            if match:
                return True
            return traverse(node.left) or traverse(node.right)

        return traverse(s)

    def test(self):
        from leetcode import arr2tree
        s = arr2tree([1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,2])
        t = arr2tree([1,None,1,None,1,None,1,None,1,None,1,2])
        print self.isSubtree(s, t)
