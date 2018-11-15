#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (40.95%)
# Total Accepted:    276K
# Total Submissions: 670.4K
# Testcase Example:  '[1,1,2]'
#
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
# 
# Example 1:
# 
# 
# Input: 1->1->2
# Output: 1->2
# 
# 
# Example 2:
# 
# 
# Input: 1->1->2->3->3
# Output: 1->2->3
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        while node:
            while node.next and node.next.val == node.val:
                node.next = node.next.next
            node = node.next
        return head
