#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (40.49%)
# Total Accepted:    28.2K
# Total Submissions: 66.2K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# Given a binary tree, return all duplicate subtrees. For each kind of
# duplicate subtrees, you only need to return the root node of any one of
# them.
# 
# Two trees are duplicate if they have the same structure with same node
# values.
# 
# Example 1: 
# 
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
# 
# 
# The following are two duplicate subtrees:
# 
# 
# ⁠     2
# ⁠    /
# ⁠   4
# 
# 
# and
# 
# 
# ⁠   4
# 
# Therefore, you need to return above trees' root in the form of a list.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, Counter
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        lookup = defaultdict()
        lookup.default_factory = lookup.__len__
        counter = Counter()
        ret = []
        def traverse(node):
            if node:
                uid = lookup[traverse(node.left), node.val, traverse(node.right)]
                counter[uid] += 1
                if counter[uid] == 2:
                    ret.append(node)
                return uid
        traverse(root)
        return ret
