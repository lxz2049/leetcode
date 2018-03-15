/*
 * [106] Construct Binary Tree from Inorder and Postorder Traversal
 *
 * https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
 *
 * algorithms
 * Medium (33.18%)
 * Total Accepted:    103.5K
 * Total Submissions: 310.9K
 * Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
 *
 * Given inorder and postorder traversal of a tree, construct the binary tree.
 * 
 * Note:
 * You may assume that duplicates do not exist in the tree.
 * 
 * For example, given
 * 
 * 
 * inorder = [9,3,15,20,7]
 * postorder = [9,15,7,20,3]
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
	TreeNode* buildSubTree(vector<int>& inorder, vector<int>& postorder, int in_s, int in_e, int p_s, int p_e) {
		//printf("%d %d %d %d\n", in_s, in_e, p_s, p_e);
		if (in_s > in_e || p_s > p_e)
			return NULL;
		TreeNode* root = new TreeNode(postorder[p_e]);
		for (int i=in_s; i<=in_e; ++i) {
			if (postorder[p_e] == inorder[i]) {
				root->left = buildSubTree(inorder, postorder, in_s, i-1, p_s, p_s+i-1-in_s);
				root->right = buildSubTree(inorder, postorder, i+1, in_e, p_s+i-in_s, p_e-1);
			}
		}
		return root;
	}

    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
		int size = inorder.size();
        return buildSubTree(inorder, postorder, 0, size-1, 0, size-1);
    }

	bool test() {
		int in[] = {9, 3, 15, 20, 7};
		int post[] = {9, 15, 7, 20, 3};
		vector<int> inorder(in, in+5);
		vector<int> postorder(post, post+5);
		buildTree(inorder, postorder);
		return true;
	}
};
