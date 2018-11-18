#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (50.40%)
# Total Accepted:    450.3K
# Total Submissions: 890.9K
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverse(node):
            if not node or not node.next:
                return node, node
            head, tail = reverse(node.next)
            tail.next = node
            node.next = None
            return head, node

        return reverse(head)[0]

