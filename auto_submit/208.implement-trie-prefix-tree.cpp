/*
 * [208] Implement Trie (Prefix Tree)
 *
 * https://leetcode.com/problems/implement-trie-prefix-tree/description/
 *
 * algorithms
 * Medium (33.13%)
 * Total Accepted:    131.8K
 * Total Submissions: 395.3K
 * Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
 *
 * Implement a trie with insert, search, and startsWith methods.
 * 
 * Example:
 * 
 * 
 * Trie trie = new Trie();
 * 
 * trie.insert("apple");
 * trie.search("apple");   // returns true
 * trie.search("app");     // returns false
 * trie.startsWith("app"); // returns true
 * trie.insert("app");   
 * trie.search("app");     // returns true
 * 
 * 
 * Note:
 * 
 * 
 * You may assume that all inputs are consist of lowercase letters a-z.
 * All inputs are guaranteed to be non-empty strings.
 * 
 * 
 */
class Trie {
private:
    Trie* next[26] = {};
    bool isWord;
public:
    /** Initialize your data structure here. */
    Trie() : isWord(0) {}
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        Trie* root = this;
        for (int i=0; i<word.size(); ++i) {
            Trie*& n = root->next[word[i]-'a'];
            if (!n) n = new Trie();
            root = n;
        }      
        root->isWord = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        Trie* root = this;
        for (int i=0; i<word.size(); ++i) {
            Trie*& n = root->next[word[i]-'a'];
            if (!n) return false;
            root = n;
        }
        return root->isWord;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string word) {
        Trie* root = this;
        for (int i=0; i<word.size(); ++i) {
            Trie*& n = root->next[word[i]-'a'];
            if (!n) return false;
            root = n;
        }
        return true;
    }
};

class Solution {
public:
    void test() {
        Trie obj;
        obj.insert("app");
        obj.insert("apple");
        obj.insert("beer");
        obj.insert("add");
        obj.insert("jam");
        obj.insert("rental");
        cout<<obj.search("apps")<<endl;
        cout<<obj.search("app")<<endl;
        cout<<obj.search("ad")<<endl;
    }
};
