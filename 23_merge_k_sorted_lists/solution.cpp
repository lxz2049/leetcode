#include <iostream>                                                                                                           
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct ListNode {
	int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
	ListNode *mergeLists(vector<ListNode*> &lists, int left, int right) {
		//printf("%d %d\n", left, right);
		if (left > right) {
			return NULL;
		}
		if (left == right) {
			return lists[left];
		}
		int mid = (left + right) / 2;
		ListNode *listA = mergeLists(lists, left, mid);
		ListNode *listB = mergeLists(lists, mid + 1, right);

		// merge list A and B
		ListNode *head = NULL;
		ListNode *iter = NULL;
		ListNode *iterA = listA;
		ListNode *iterB = listB;
		while (iterA && iterB) {
			//printf("%d\n", lists[i] ? lists[i]->val: -1);
			ListNode *next;
			if (iterA->val < iterB->val) {
				next =  iterA;
				iterA = iterA->next;
			} else {
				next =  iterB;
				iterB = iterB->next;
			}
			if (iter) {
				iter->next = next;
				iter = iter->next;
			} else {
				head = iter = next;
			}
		}

		if (iterA) {
			if (iter)
				iter->next = iterA;
			else
				head = iter = iterA;
		}

		if (iterB) {
			if (iter)
				iter->next = iterB;
			else
				head = iter = iterB;
		}

		return head;
	}

	ListNode *mergeKLists(vector<ListNode*> &lists) {
		return mergeLists(lists, 0, lists.size()-1);
	}
};

int main() {
	vector<ListNode*> v;

	v.push_back(NULL);

	ListNode firstObj(1);
	v.push_back(&firstObj);

	ListNode secondObj(0);
	v.push_back(&secondObj);

	ListNode thirdObj(3);
	v.push_back(&thirdObj);

	ListNode forthObj(4);
	v.push_back(&forthObj);

	ListNode fifthObj(5);
	v.push_back(&fifthObj);

	Solution sol;
	ListNode *head = sol.mergeKLists(v);
	while (head) {
		printf("%d ", head->val);
		head = head->next;
	}
	printf("\n");
    return 0;
}
