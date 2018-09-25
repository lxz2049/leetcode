/*
 * [676] Implement Magic Dictionary
 *
 * https://leetcode.com/problems/implement-magic-dictionary/description/
 *
 * algorithms
 * Medium (49.38%)
 * Total Accepted:    17K
 * Total Submissions: 34.5K
 * Testcase Example:  '["MagicDictionary", "buildDict", "search", "search", "search", "search"]\n[[], [["hello","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]'
 *
 * 
 * Implement a magic directory with buildDict, and search methods.
 * 
 * 
 * 
 * For the method buildDict, you'll be given a list of non-repetitive words to
 * build a dictionary.
 * 
 * 
 * 
 * For the method search, you'll be given a word, and judge whether if you
 * modify exactly one character into another character in this word, the
 * modified word is in the dictionary you just built.
 * 
 * 
 * Example 1:
 * 
 * Input: buildDict(["hello", "leetcode"]), Output: Null
 * Input: search("hello"), Output: False
 * Input: search("hhllo"), Output: True
 * Input: search("hell"), Output: False
 * Input: search("leetcoded"), Output: False
 * 
 * 
 * 
 * Note:
 * 
 * You may assume that all the inputs are consist of lowercase letters a-z.
 * For contest purpose, the test data is rather small by now. You could think
 * about highly efficient algorithm after the contest.
 * Please remember to RESET your class variables declared in class
 * MagicDictionary, as static/class variables are persisted across multiple
 * test cases. Please see here for more details.
 * 
 * 
 */
class MagicDictionary {
private:
    map<string, string> s;
public:
    /** Initialize your data structure here. */
    MagicDictionary() {
        
    }
    
    /** Build a dictionary through a list of words */
    void buildDict(vector<string> dict) {
        s.clear();
        for(int i=0; i<dict.size(); ++i) {
            for (int j=0; j<dict[i].size(); ++j) {
                string str = dict[i];
                str[j] = '*';
                if (s.find(str) != s.end()) {
                    s[str] = "*";
                } else {
                    s[str] = dict[i];
                }
            }
        }
    }
    
    /** Returns if there is any word in the trie that equals to the given word after modifying exactly one character */
    bool search(string word) {
        for (int i=0; i<word.size(); ++i) {
            string str = word;
            str[i] = '*';
            if (s.find(str) != s.end() && s[str] != word)
                return true;
        }
        return false;
    }
};

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dict);
 * bool param_2 = obj.search(word);
 */
