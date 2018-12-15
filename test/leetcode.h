#include <algorithm>
#include <iostream>
#include <list>
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

struct Point {
  int x;  
  int y;
  Point(): x(0), y(0) {}
  Point(int a, int b): x(a), y(b) {}
};

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

TreeNode* arr2treeUtil(vector<int> arr, int i) {
    if (i >= arr.size() || arr[i] == -1)   return NULL;
    TreeNode* node = new TreeNode(arr[i]);
    node->left = arr2treeUtil(arr, i*2+1);
    node->right = arr2treeUtil(arr, i*2+2);
    return node;
}

TreeNode* arr2tree(vector<int> arr) {
    TreeNode* root = new TreeNode(arr[0]);
    root->left = arr2treeUtil(arr, 1);
    root->right = arr2treeUtil(arr, 2);
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

void printVector(const vector<int>& nums) {
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
