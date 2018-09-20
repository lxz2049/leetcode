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

		TreeNode* root = new TreeNode(preorder[0]);
        stack<TreeNode*> s;
        s.push(root);
		TreeNode* node = NULL;
		for (int i=1, j=0; i<preorder.size(); ++i) {
			while (!s.empty() && s.top()->val == inorder[j]) {
				node = s.top();
				s.pop();
				j++;
			}
			if (node) {
                TreeNode* newNode = new TreeNode(preorder[i]);
				node->right = newNode;
                s.push(newNode);
				node = NULL;
			} else {
                TreeNode* newNode = new TreeNode(preorder[i]);
				s.top()->left = newNode;
                s.push(newNode);
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
