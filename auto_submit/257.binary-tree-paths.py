#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (43.78%)
# Total Accepted:    194.8K
# Total Submissions: 443.9K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# Output: ["1->2->5", "1->3"]
# 
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ret = []
        def traverse(node, path):
            if not node.left and not node.right:
                ret.append(path + [str(node.val)])
                return
            if node.left:
                traverse(node.left, path + [str(node.val)])
            if node.right:
                traverse(node.right, path + [str(node.val)])
        if root:
            traverse(root, [])
        return ["->".join(path) for path in ret]
