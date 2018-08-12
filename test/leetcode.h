#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>
#include <iostream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

TreeNode* arr2treeUtil(int x[], int i, int len) {
    if (i >= len || x[i] == -1)   return NULL;
    TreeNode* node = new TreeNode(x[i]);
    node->left = arr2treeUtil(x, i*2+1, len);
    node->right = arr2treeUtil(x, i*2+2, len);
    return node;
}

TreeNode* arr2tree(int x[], int len) {
    TreeNode* root = new TreeNode(x[0]);
    root->left = arr2treeUtil(x, 1, len);
    root->right = arr2treeUtil(x, 2, len);
    return root;
}

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
    for (int i=1; i<len; ++i) {
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
