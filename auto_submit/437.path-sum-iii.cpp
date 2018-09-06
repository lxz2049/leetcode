class Solution {
public:
    int calPathSum(TreeNode* node, unordered_map<int, int>& prefixSum, int target, int sum) {
        int ret = 0;
        if (node)  {
            sum += node->val;
            ret += prefixSum[sum-target];
            prefixSum[sum]++;
            ret += calPathSum(node->left, prefixSum, target, sum) + calPathSum(node->right, prefixSum, target, sum);
            prefixSum[sum]--;
        }
        return ret;
    }

    int pathSum(TreeNode* root, int target) {
        unordered_map<int, int> prefixSum;
        prefixSum[0] = 1;
        return calPathSum(root, prefixSum, target, 0);
    }
};
