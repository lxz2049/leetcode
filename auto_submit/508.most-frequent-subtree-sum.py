#
# [508] Most Frequent Subtree Sum
#
# https://leetcode.com/problems/most-frequent-subtree-sum/description/
#
# algorithms
# Medium (52.24%)
# Total Accepted:    36.3K
# Total Submissions: 68.9K
# Testcase Example:  '[5,2,-3]'
#
# 
# Given the root of a tree, you are asked to find the most frequent subtree
# sum. The subtree sum of a node is defined as the sum of all the node values
# formed by the subtree rooted at that node (including the node itself). So
# what is the most frequent subtree sum value? If there is a tie, return all
# the values with the highest frequency in any order.
# 
# 
# Examples 1
# Input:
# 
# ⁠ 5
# ⁠/  \
# 2   -3
# 
# return [2, -3, 4], since all the values happen only once, return all of them
# in any order.
# 
# 
# Examples 2
# Input:
# 
# ⁠ 5
# ⁠/  \
# 2   -5
# 
# return [2], since 2 happens twice, however -5 only occur once.
# 
# 
# Note:
# You may assume the sum of values in any subtree is in the range of 32-bit
# signed integer.
# 
#
# Definition for a binary tree node.
#add class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
import operator
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.max_occ = 0
        counter = collections.Counter()
        def traverse(node):
            if not node:
                return 0
            treesum = node.val + traverse(node.left) + traverse(node.right)
            counter.update([treesum])
            self.max_occ = max(counter[treesum], self.max_occ)
            return treesum
        traverse(root)
        return [e[0] for e in counter.most_common() if e[1] == self.max_occ]

