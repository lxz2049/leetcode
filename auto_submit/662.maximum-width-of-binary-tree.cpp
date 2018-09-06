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
    int traverse(TreeNode* node, vector<pair<int, int>>& widths, int level, int index) {
        if (node) {
            if (level >= widths.size()) {
                pair<int, int> p(index, index);
                widths.push_back(p);
            }
            widths[level].first = min(widths[level].first, index);
            widths[level].second = max(widths[level].second, index);
            int width = widths[level].second - widths[level].first + 1;
            int childrenWidth = max(traverse(node->left, widths, level+1, index*2), traverse(node->right, widths, level+1, index*2+1));
            return max(width, childrenWidth);
        }
        return 0;
    }
    int widthOfBinaryTree(TreeNode* root) {
        vector<pair<int, int>> widths;    
        int ret = traverse(root, widths, 0, 0);
        //for (int i=0; i<widths.size(); ++i) { cout<<widths[i].first<<" "<<widths[i].second<<endl; }
        return ret;
    }

    void test() {
    
    }
};
