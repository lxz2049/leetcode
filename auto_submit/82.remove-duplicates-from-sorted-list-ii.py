#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (31.07%)
# Total Accepted:    151.7K
# Total Submissions: 488.2K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# 
# Example 1:
# 
# 
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# 
# 
# Example 2:
# 
# 
# Input: 1->1->1->2->3
# Output: 2->3
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
        cur, prev = head, None
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur.next = cur.next.next
                if prev:
                    prev.next = cur.next
                else:
                    head = cur.next
                cur = cur.next
            else:
                cur, prev = cur.next, cur
        return head
        
