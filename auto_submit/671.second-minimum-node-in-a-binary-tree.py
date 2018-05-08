#
# [671] Second Minimum Node In a Binary Tree
#
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
#
# algorithms
# Easy (41.70%)
# Total Accepted:    24K
# Total Submissions: 57.4K
# Testcase Example:  '[2,2,5,null,null,5,7]'
#
# 
# Given a non-empty special binary tree consisting of nodes with the
# non-negative value, where each node in this tree has exactly two or zero
# sub-node. If the node has two sub-nodes, then this node's value is the
# smaller value among its two sub-nodes. 
# 
# 
# 
# Given such a binary tree, you need to output the second minimum value in the
# set made of all the nodes' value in the whole tree. 
# 
# 
# 
# If no such second minimum value exists, output -1 instead.
# 
# 
# Example 1:
# 
# Input: 
# ⁠   2
# ⁠  / \
# ⁠ 2   5
# ⁠    / \
# ⁠   5   7
# 
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
# 
# 
# 
# Example 2:
# 
# Input: 
# ⁠   2
# ⁠  / \
# ⁠ 2   2
# 
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest
# value.
# 
# 
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        
        smallest = root.val
        def traverse(node):
            if node:
                l = filter(lambda x: x>smallest, (traverse(node.left), traverse(node.right), node.val))
                ret = min(l) if l else smallest
                #print l, ret
                return ret
        ans = traverse(root)
        return ans if ans > smallest else -1

    def test(self):
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        print self.findSecondMinimumValue(root)
