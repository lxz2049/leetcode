class Solution {
public:
    int calPathSum(TreeNode* node, unordered_map<int, int>& prefixSum, int target, int sum) {
        int ret = 0;
        if (node)  {
            sum += node->val;
            ret += prefixSum[sum-target];
            prefixSum[sum]++;
            ret +=  calPathSum(node->left, prefixSum, target, sum) + calPathSum(node->right, prefixSum, target, sum);
            //cout<<sum-target<<" "<<prefixSum[sum-target]<<endl;
            prefixSum[sum]--;
        }
        return ret;
    }

    int pathSum(TreeNode* root, int target) {
        unordered_map<int, int> prefixSum;
        prefixSum[0] = 1;
        return calPathSum(root, prefixSum, target, 0);
    }

    void test() {
        //int a[] = {5,4,8,11,-1,13,4,7,2,-1,-1,5,1};
        //TreeNode* root = arr2tree(a, sizeof(a) / sizeof(int));
        //cout<<3<<" ? "<<pathSum(root, 22)<<endl;
        
        //int a[] = {1};
        //TreeNode* root = arr2tree(a, sizeof(a) / sizeof(int));
        //cout<<0<<" ? "<<pathSum(root, 0)<<endl;
    }
};
