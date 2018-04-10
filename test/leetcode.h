#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>
#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

struct ListNode {
	int val;
	ListNode* next;
	ListNode(int x): val(x), next(NULL) {}
    void print() {
        ListNode* node = next;
        while (node) {
            printf("%d ", node->val);
            node = node->next;
        }
        printf("\n");
    }
};

ListNode* arr2list(int x[], int len) {
    ListNode* head = new ListNode(x[0]);
    ListNode* node = head;
    for (int i=0; i<len; ++i) {
        node = node->next = new ListNode(x[i]);
    }
    return head;
}


struct Interval {
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
};
