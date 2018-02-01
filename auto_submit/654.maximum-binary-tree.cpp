/*
 * [654] Maximum Binary Tree
 *
 * https://leetcode.com/problems/maximum-binary-tree/description/
 *
 * algorithms
 * Medium (69.79%)
 * Total Accepted:    23.5K
 * Total Submissions: 33.6K
 * Testcase Example:  '[3,2,1,6,0,5]'
 *
 * 
 * Given an integer array with no duplicates. A maximum tree building on this
 * array is defined as follow:
 * 
 * The root is the maximum number in the array. 
 * The left subtree is the maximum tree constructed from left part subarray
 * divided by the maximum number.
 * The right subtree is the maximum tree constructed from right part subarray
 * divided by the maximum number. 
 * 
 * 
 * 
 * 
 * Construct the maximum tree by the given array and output the root node of
 * this tree.
 * 
 * 
 * Example 1:
 * 
 * Input: [3,2,1,6,0,5]
 * Output: return the tree root node representing the following tree:
 * 
 * ⁠     6
 * ⁠   /   \
 * ⁠  3     5
 * ⁠   \    / 
 * ⁠    2  0   
 * ⁠      \
 * ⁠       1
 * 
 * 
 * 
 * Note:
 * 
 * The size of the given array will be in the range [1,1000].
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
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
		return constructMaximumSubTree(nums, 0, nums.size()-1);
    }

	TreeNode* constructMaximumSubTree(vector<int>& nums, int head, int tail) {
		if (head > tail)
			return NULL;

		int max = nums[head];
		int max_i = head;
 		for (int i=head+1; i<=tail;++i) {
			if (nums[i] > max) {
				max = nums[i];
				max_i = i;
			}
		}
		//printf("max:%d max_i:%d\n", max, max_i);
		TreeNode* root = new TreeNode(max);
		root->left = constructMaximumSubTree(nums, head, max_i-1);
		root->right = constructMaximumSubTree(nums, max_i+1, tail);
		return root;
	}

	bool test() {
		int t[] = {3, 2, 1, 6, 0, 5};
		vector<int> v(t, t+5);
		traverse(constructMaximumBinaryTree(v));
		return true;
	}

	void traverse(TreeNode* node) {
		if (!node)
			return;
		traverse(node->left);
		printf("%d\n", node->val);
		traverse(node->right);
	}
};
