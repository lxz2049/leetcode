class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> ret;
        if (root) {
            queue<pair<TreeNode*, int>> q;
            q.push({root, 0});
            while (!q.empty()) {
                TreeNode* node = q.front().first;
                int level = q.front().second;
                q.pop();
                //cout<<node->val<<" "<<level<<endl;
                if (ret.size() <= level) ret.resize(level+1);
                ret[level].push_back(node->val);
                if (node->left) {
                    q.push({node->left, level+1});
                    //cout<<node->left->val<<" "<<level+1<<endl;
                }
                if (node->right) {
                    q.push({node->right, level+1});
                    //cout<<node->right->val<<" "<<level+1<<endl;
                }
            }
            reverse(ret.begin(), ret.end());
        }
        return ret;
    }

    void test() {
        //TreeNode* root = arr2tree({3,9,20,-1,-1,15,7});
        //levelOrderBottom(root);
    }
};
