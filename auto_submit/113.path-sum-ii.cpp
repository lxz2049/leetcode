/*
 * [113] Path Sum II
 *
 * https://leetcode.com/problems/path-sum-ii/description/
 *
 * algorithms
 * Medium (37.21%)
 * Total Accepted:    182.9K
 * Total Submissions: 491.1K
 * Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
 *
 * Given a binary tree and a sum, find all root-to-leaf paths where each path's
 * sum equals the given sum.
 * 
 * Note: A leaf is a node with no children.
 * 
 * Example:
 * 
 * Given the below binary tree and sum = 22,
 * 
 * 
 * ⁠     5
 * ⁠    / \
 * ⁠   4   8
 * ⁠  /   / \
 * ⁠ 11  13  4
 * ⁠/  \    / \
 * 7    2  5   1
 * 
 * 
 * Return:
 * 
 * 
 * [
 * ⁠  [5,4,11,2],
 * ⁠  [5,8,4,5]
 * ]
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
    vector<vector<int>> ans;

    void getPathSum(TreeNode* node, vector<int>& path, int target, int sum) {
        if (node) {
            sum += node->val;
            path.push_back(node->val);
            if (!node->left && !node->right && sum == target) {
                ans.push_back(path);
            }   
            getPathSum(node->left, path, target, sum);
            getPathSum(node->right, path, target, sum);
            path.pop_back();
        }
    }

    vector<vector<int>> pathSum(TreeNode* root, int target) {
        vector<int> path;
        getPathSum(root, path, target, 0);
        return ans;
    }
};
