#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (32.68%)
# Total Accepted:    161.4K
# Total Submissions: 491.1K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
# 
# 
#
# Definition for singly-linked list.
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        cnt = 1
        node_m, prev_m = head, None
        while cnt < m:
            prev_m, node_m = node_m, node_m.next
            cnt += 1
        prev, cur, cnt = node_m, node_m.next, cnt + 1
        while cnt <= n:
            prev, cur.next, cur = cur, prev, cur.next
            cnt += 1
        #print prev_m.val, node_m.val, prev.val, cur.val if cur else -1

        if prev_m:
            prev_m.next = prev
        else:
            head = prev

        node_m.next = cur
        return head
    
    def test(self):
        class ListNode(object):
            def __init__(self, x):
                self.val = x
                self.next = None
        one = ListNode(1)
        two = ListNode(2)
        three = ListNode(3)
        four = ListNode(4)
        five = ListNode(5)
        one.next, two.next, three.next, four.next = two, three, four, five
        head = self.reverseBetween(one, 2, 4)
        while head:
            print head.val
            head = head.next

            
