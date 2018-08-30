#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (43.88%)
# Total Accepted:    147.4K
# Total Submissions: 331.7K
# Testcase Example:  '[]'
#
# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# Note: next() and hasNext() should run in average O(1) time and uses O(h)
# memory, where h is the height of the tree. 
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0
        
    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        ret = node.val
        if node.right:
            self.stack.append(node.right)
            node = node.right
            while node.left:
                self.stack.append(node.left)
                node = node.left
        return ret
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

class Solution:
    def test(self):
        from leetcode import arr2tree
        it = BSTIterator(arr2tree([4,2,1,3,6,5,7]))
        while it.hasNext():
            print it.next()
