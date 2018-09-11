/*
 * [148] Sort List
 *
 * https://leetcode.com/problems/sort-list/description/
 *
 * algorithms
 * Medium (31.51%)
 * Total Accepted:    147.7K
 * Total Submissions: 467.6K
 * Testcase Example:  '[4,2,1,3]'
 *
 * Sort a linked list in O(n log n) time using constant space complexity.
 * 
 * Example 1:
 * 
 * 
 * Input: 4->2->1->3
 * Output: 1->2->3->4
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: -1->5->3->4->0
 * Output: -1->0->3->4->5
 * 
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
    ListNode* getMidList(ListNode* head) {
        //cout<<"getMidList"<<endl; printList(head);
        ListNode* slow = head;
        ListNode* fast = head->next;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* ret = slow->next;
        slow->next = NULL;
        return ret;
    }

    ListNode* mergeList(ListNode* left, ListNode* right) {
        //cout<<"mergeList"<<endl; printList(left); printList(right);
        ListNode* head = NULL;
        ListNode* tail = NULL;
        while (left && right) {
            ListNode* cur;
            if (left->val < right->val) {
                cur = left;
                left = left->next;
            } else {
                cur = right;
                right = right->next;
            }

            if (!head) {
                head = tail = cur;
            } else {
                tail->next = cur;
                tail = cur;
            }
        }
        if (left) {
            if (!head) {
                head = tail = left;
            } else {
                tail->next = left;
            }
        }
        if (right) {
            if (!head) {
                head = tail = right;
            } else {
                tail->next = right;
            }
        }
        return head;
    }

    ListNode* sortList(ListNode* head) {
        if (!head)
            return NULL;
        //cout<<"sortList"<<endl; printList(head);
        ListNode* mid = getMidList(head);
        if (mid)
            return mergeList(sortList(head), sortList(mid));
        return head;
    }

    void test() {
        //int a[] = {4,2,1,3};
        //ListNode* headA = arr2list(a, 4);
        //printList(sortList(headA));
        //int b[] = {2,3};
        //ListNode* headB = arr2list(b, 2);
        //ListNode* mid = getMidList(headB);
        //ListNode* sorted = mergeList(headB, mid);
        //printList(sorted);
    }
};
