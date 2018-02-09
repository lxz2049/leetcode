#include <vector>
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
};
