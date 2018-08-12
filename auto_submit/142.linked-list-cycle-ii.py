#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (30.43%)
# Total Accepted:    161.7K
# Total Submissions: 536.9K
# Testcase Example:  '[]\nno cycle'
#
# 
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
# 
# 
# 
# Note: Do not modify the linked list.
# 
# 
# Follow up:
# Can you solve it without using extra space?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        try:
            slow = head.next
            fast = head.next.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        except:
            pass
        return None
