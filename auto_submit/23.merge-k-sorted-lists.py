#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (30.40%)
# Total Accepted:    275.4K
# Total Submissions: 904.8K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [(node.val, node) for node in lists if node]
        heapq.heapify(h)
        head = node = ListNode(0)
        while h:
            _, n = heapq.heappop(h)
            if n.next:
                heapq.heappush(h, (n.next.val, n.next))
            node.next = n
            node = n
        return head.next
