#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unordered_map>
#include <unordered_set>
#include <vector>

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

void printList(ListNode* head) {
    while (head) {
        cout<<head->val<<" ";
        head = head->next;
        if (!head) cout<<endl;
    }
}

void printVector(vector<int>& nums) {
    for (int i=0; i<nums.size(); ++i) {
        cout<<nums[i]<<" ";
        if (i == nums.size() - 1)
            cout<<endl;
    }
}


struct Interval {
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
};
