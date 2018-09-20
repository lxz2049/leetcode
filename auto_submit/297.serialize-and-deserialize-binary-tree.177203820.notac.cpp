class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        // pre-order   
        string ret;
        stack<TreeNode*> s;
        TreeNode* node = root;
        while (node || !s.empty()) {
            if (node) {
                ret += to_string(node->val) + ",";
                s.push(node);
                node = node->left;
            } else {
                ret += ("#,");
                node = s.top()->right;
                s.pop();
            }
        }
        //cout<<ret<<endl;
        return ret;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (!data.size()) return NULL;

        stack<TreeNode*> s;
        TreeNode *node = NULL, *dummy = new TreeNode(0);
        s.push(dummy);
        for (int p, i=0; i<data.size(); i=p+1) {
            TreeNode* newNode = NULL;
            p = data.find(',', i);
            if (data[i] != '#') {
                int num = atoi(data.substr(i, p).c_str());
                newNode = new TreeNode(num);
            } 
            if (!s.top()) {
                s.pop();
                node = s.top();
            }

            if (node) {
                node->right = newNode;
                s.pop();
                s.push(newNode);
                node = NULL;
            } else {
                s.top()->left = newNode;                   
                s.push(newNode);
            }
        }
        return dummy->left;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
//
class Solution {
public:
    void test() {
        TreeNode* root = NULL;
        //root = arr2tree({1,2,3,-1,-1,4,5});
        //root = arr2tree({-1,0,1});
        Codec codec;
        codec.serialize(codec.deserialize(codec.serialize(root)));
    }
};

