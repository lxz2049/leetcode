/*
 * [105] Construct Binary Tree from Preorder and Inorder Traversal
 *
 * https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
 *
 * algorithms
 * Medium (33.62%)
 * Total Accepted:    131.3K
 * Total Submissions: 390.4K
 * Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
 *
 * Given preorder and inorder traversal of a tree, construct the binary tree.
 * 
 * Note:
 * You may assume that duplicates do not exist in the tree.
 * 
 * For example, given
 * 
 * 
 * preorder = [3,9,20,15,7]
 * inorder = [9,3,15,20,7]
 * 
 * Return the following binary tree:
 * 
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
 * 
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
		if (!preorder.size() || preorder.size() != inorder.size())
			return NULL;

		TreeNode* left = NULL;
		TreeNode* right = NULL;
		TreeNode* root = NULL;
        stack<TreeNode*> s;
		for (int i=0, j=0; i<preorder.size(); ++i) {
			//printf("%d %d\n", i, j);
			while (!s.empty() && s.top()->val == inorder[j]) {
				right = s.top();
				s.pop();
				j++;
			}
			TreeNode* newNode = new TreeNode(preorder[i]);
			s.push(newNode);
			if (!root)	root = newNode;
			if (right) {
				//printf("%d r %d\n", right->val, newNode->val);
				right->right = newNode;
				left = newNode;
				right = NULL;
			} else {
				//printf("%d l %d\n", left?left->val:-1, newNode->val);
				if (left)	left->left = newNode;
				left = newNode;
			}
		}

		return root;
    }

	bool test() {
		int pre[] = {3, 9, 20, 15, 7};
		int in[] = {9, 3, 15, 20, 7};
		vector<int> a(pre, pre + 5);
		vector<int> b(in, in + 5);
		buildTree(a, b);
		return true;
	}
};
