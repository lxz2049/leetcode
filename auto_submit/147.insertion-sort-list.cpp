/*
 * [147] Insertion Sort List
 *
 * https://leetcode.com/problems/insertion-sort-list/description/
 *
 * algorithms
 * Medium (33.82%)
 * Total Accepted:    117.8K
 * Total Submissions: 348.1K
 * Testcase Example:  '[]'
 *
 * Sort a linked list using insertion sort.
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
		ListNode* end = head;
		ListNode* prev_end = NULL;
		while (end) {
			ListNode* it = head;
			ListNode* prev_it = NULL;
			while (it != end && it->val < end->val) {
				//printf("1 it:%d end:%d\n", it->val, end->val);
				prev_it = it;
				it = it->next;
			}
			printf("2 it:%d end:%d\n", it, end);
			if (it != end) {
				prev_end->next = end->next;
				if (prev_it)
					prev_it->next = end;
				else
					head=end;
				end->next = it;
				end = prev_end->next;
			} else {
				prev_end = end;
				end = end->next;
			}
		}
		return head;
    }

	bool test() {
		ListNode* head = new ListNode(1);
		ListNode* it = head;
		it = it->next = new ListNode(1);
		it = it->next = new ListNode(1);
		ListNode* node = insertionSortList(head);
		while (node) {
			printf("%d ", node->val);
			node=node->next;
		}
		printf("\n");
		return true;
	}
};
