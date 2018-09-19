/*
 * [449] Serialize and Deserialize BST
 *
 * https://leetcode.com/problems/serialize-and-deserialize-bst/description/
 *
 * algorithms
 * Medium (43.18%)
 * Total Accepted:    34.8K
 * Total Submissions: 80.4K
 * Testcase Example:  '[2,1,3]'
 *
 * Serialization is the process of converting a data structure or object into a
 * sequence of bits so that it can be stored in a file or memory buffer, or
 * transmitted across a network connection link to be reconstructed later in
 * the same or another computer environment. 
 * 
 * Design an algorithm to serialize and deserialize a binary search tree. There
 * is no restriction on how your serialization/deserialization algorithm should
 * work. You just need to ensure that a binary search tree can be serialized to
 * a string and this string can be deserialized to the original tree
 * structure.
 * 
 * 
 * The encoded string should be as compact as possible.
 * 
 * 
 * 
 * Note: Do not use class member/global/static variables to store states. Your
 * serialize and deserialize algorithms should be stateless.
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
class Codec {
public:
    // Encodes a tree to a single string.
    vector<int> serialize(TreeNode* root) {
        if (!root)  return {};
        vector<int> left = serialize(root->left);
        vector<int> right = serialize(root->right);
        vector<int> ret;
        ret.reserve(left.size() + right.size() + 1);
        ret.push_back(root->val);
        ret.insert(ret.end(), left.begin(), left.end());
        ret.insert(ret.end(), right.begin(), right.end());
        //cout<<ret<<endl;
        return ret;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(vector<int> data) {
        if (!data.size())   return NULL;

        vector<TreeNode*> s;
        TreeNode* root = new TreeNode(data[0]);
        s.push_back(root);
        for (int i=1; i<data.size(); ++i) {
            TreeNode* node = new TreeNode(data[i]);
            TreeNode* parent = NULL;
            while (s.size() && node->val > s.back()->val) {
                parent = s.back();
                s.pop_back();
            } 
            if (parent) {
                //cout<<"right "<<node->val<<endl;
                parent->right = node;
            } else {
                //cout<<"left "<<node->val<<endl;
                s.back()->left = node;
            }
            s.push_back(node);
        }
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
class Solution {
public:
    void test() {
        //TreeNode *root = arr2tree({2,1,3});
        //Codec codec;
        //codec.deserialize(codec.serialize(root));
    }
};
