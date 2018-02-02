/*
 * [653] Two Sum IV - Input is a BST
 *
 * https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
 *
 * algorithms
 * Easy (50.28%)
 * Total Accepted:    29.3K
 * Total Submissions: 58.2K
 * Testcase Example:  '[5,3,6,2,4,null,7]\n9'
 *
 * Given a Binary Search Tree and a target number, return true if there exist
 * two elements in the BST such that their sum is equal to the given target.
 * 
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
    bool findTarget(TreeNode* root, int k) {	       
		// for each node, find another node that would make the sum equal to k
		return traverse(root, root, k);	
    }

	bool traverse(TreeNode* root, TreeNode* node, int k) {
		if (node) {
			//cout<<"traverse "<<node->val<<endl;
			return traverse(root, node->left, k) 
				|| findNumber(node, root, k - node->val) 
				|| traverse(root, node->right, k);
		}
		return false;
	}

	bool findNumber(TreeNode* orig, TreeNode* node, int k) {
		if (node && node != orig) {
			//cout<<"current number "<<node->val<<" find number "<<k<<endl;
			return (k == node->val)
				|| (k < node->val ? findNumber(orig, node->left, k) : findNumber(orig, node->right, k));
		}
		return false;
	}

	/*
	bool test() {
		TreeNode root(5);
		root.left=&TreeNode(3);
		root.right=&TreeNode(6);
		root.left->left=&TreeNode(2);
		root.left->right=&TreeNode(4);
		root.right->right=&TreeNode(7);
		TreeNode tree(1);
		return findTarget(&root, 9) && !findTarget(&tree, 2);
	}
	*/
};

