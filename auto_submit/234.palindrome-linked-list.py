#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (33.42%)
# Total Accepted:    158.8K
# Total Submissions: 473.6K
# Testcase Example:  '[]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        if length < 2:
            return True

        cnt = 0
        left = None
        right = head
        while True:
            next_node = right.next
            right.next = left
            left = right
            right = next_node

            cnt += 1
            if cnt == length / 2:
                break

        if length % 2 > 0:
            right = right.next

        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
