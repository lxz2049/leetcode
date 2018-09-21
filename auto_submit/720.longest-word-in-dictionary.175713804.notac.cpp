/*
 * [720] Longest Word in Dictionary
 *
 * https://leetcode.com/problems/longest-word-in-dictionary/description/
 *
 * algorithms
 * Easy (41.94%)
 * Total Accepted:    20K
 * Total Submissions: 47.9K
 * Testcase Example:  '["w","wo","wor","worl","world"]'
 *
 * Given a list of strings words representing an English Dictionary, find the
 * longest word in words that can be built one character at a time by other
 * words in words.  If there is more than one possible answer, return the
 * longest word with the smallest lexicographical order.  If there is no
 * answer, return the empty string.
 * 
 * Example 1:
 * 
 * Input: 
 * words = ["w","wo","wor","worl", "world"]
 * Output: "world"
 * Explanation: 
 * The word "world" can be built one character at a time by "w", "wo", "wor",
 * and "worl".
 * 
 * 
 * 
 * Example 2:
 * 
 * Input: 
 * words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
 * Output: "apple"
 * Explanation: 
 * Both "apply" and "apple" can be built from other words in the dictionary.
 * However, "apple" is lexicographically smaller than "apply".
 * 
 * 
 * 
 * Note:
 * All the strings in the input will only contain lowercase letters.
 * The length of words will be in the range [1, 1000].
 * The length of words[i] will be in the range [1, 30].
 * 
 */
struct TrieNode {
    bool isWord;
    vector<TrieNode*> next;
    TrieNode() : isWord(false), next(vector<TrieNode*>(26)) {}
};

class Solution {
public:
    void addToTrie(TrieNode* root, string word) {
        for (int i=0; i<word.size(); ++i) {
            char c = word[i];
            TrieNode*& next = root->next[c-'a'];
            if (!next) {
                next = new TrieNode();
            }
            root = next;
        }
        root->isWord = true;
    }

    void traverse(TrieNode* node, string& wip, string& ret) {
        if (node && node->isWord) {
            if (wip.size() > ret.size())   ret = wip;

            for (int i=0; i< node->next.size(); ++i) {
                wip.push_back(char(i + int('a')));
                traverse(node->next[i], wip, ret);
                wip.pop_back();
            }
        }
    }

    string longestWord(vector<string>& words) {
        TrieNode* root = new TrieNode();
        root->isWord = true;
        for (auto word: words) {
            addToTrie(root, word);
        }

        string ret = "";
        string wip = "";
        traverse(root, wip, ret);
        return ret;
    }

    void test() {
        vector<string> words = {"a", "banana", "app", "appl", "ap", "apply", "apple"};
        cout<<longestWord(words)<<endl;
    }
};

