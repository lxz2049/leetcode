/*
 * [687] Longest Univalue Path
 *
 * https://leetcode.com/problems/longest-univalue-path/description/
 *
 * algorithms
 * Easy (32.99%)
 * Total Accepted:    25K
 * Total Submissions: 76.1K
 * Testcase Example:  '[5,4,5,1,1,5]'
 *
 * Given a binary tree, find the length of the longest path where each node in
 * the path has the same value. This path may or may not pass through the
 * root.
 * 
 * Note: The length of path between two nodes is represented by the number of
 * edges between them.
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input:
 * 
 * ⁠             5
 * ⁠            / \
 * ⁠           4   5
 * ⁠          / \   \
 * ⁠         1   1   5
 * 
 * 
 * 
 * 
 * Output:
 * 
 * 2
 * 
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * 
 * 
 * Input:
 * 
 * ⁠             1
 * ⁠            / \
 * ⁠           4   5
 * ⁠          / \   \
 * ⁠         4   4   5
 * 
 * 
 * 
 * 
 * Output:
 * 
 * 2
 * 
 * 
 * 
 * Note:
 * The given binary tree has not more than 10000 nodes.  The height of the tree
 * is not more than 1000.
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
    int ans;
    int longestUnivaluePath(TreeNode* root) {
        ans = 0;
        traverse(root);
        return ans;
    }

    int traverse(TreeNode* node) {
        if (!node)  return 0;
        int nodecnt_left = traverse(node->left);
        int nodecnt_right = traverse(node->right);

        int nodecnt_left_current = 0, nodecnt_right_current = 0;
        if (node->left && node->left->val == node->val)
            nodecnt_left_current += nodecnt_left;
        if (node->right && node->right->val == node->val)
            nodecnt_right_current += nodecnt_right;

        ans = max(ans, nodecnt_left_current+nodecnt_right_current);
        return max(nodecnt_left_current, nodecnt_right_current)+1;
    }

    void test() {
        int arr[] = {1, 4, 5, 4, 4, 5};
        //int arr[] = {5, 4, 5, 1, 1, 5};
        //cout<<longestUnivaluePath(arr2tree(arr, sizeof(arr) / sizeof(arr[0])))<<endl;
    }
};
