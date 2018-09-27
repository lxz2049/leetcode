/*
 * [131] Palindrome Partitioning
 *
 * https://leetcode.com/problems/palindrome-partitioning/description/
 *
 * algorithms
 * Medium (37.39%)
 * Total Accepted:    134.6K
 * Total Submissions: 359.4K
 * Testcase Example:  '"aab"'
 *
 * Given a string s, partition s such that every substring of the partition is
 * a palindrome.
 * 
 * Return all possible palindrome partitioning of s.
 * 
 * Example:
 * 
 * 
 * Input: "aab"
 * Output:
 * [
 * ⁠ ["aa","b"],
 * ⁠ ["a","a","b"]
 * ]
 * 
 * 
 */
class Solution {
private:
    vector<vector<string>> ret;
    vector<vector<int>> dp;
public:
    bool isPalin(string& s, int st, int en) {
        //cout<<s<<" "<<st<<" "<<en<<endl;
        if (dp[st][en] > -1)    return dp[st][en];
        for (int i = 0; i < (en-st) / 2; ++i) {
            if (s[i+st] != s[en-1-i]) {
                dp[st][en] = 0;
                return false;
            }
        }
        //cout<<s.substr(st, en-st)<<endl;
        dp[st][en] = 1;
        return true;
    }

    void traverse(string& s, vector<int>& p, int start) {
        bool found = true;
        for (int i = 1; i < p.size(); ++i) {
            found &= isPalin(s, p[i-1], p[i]);
        }
        if (found && isPalin(s, p[p.size()-1], s.size())) {
            vector<string> ans;
            for (int i = 1; i < p.size(); ++i) {
                ans.push_back(s.substr(p[i-1], p[i]-p[i-1]));
            }
            ans.push_back(s.substr(p[p.size()-1], s.size()-p.size()+1));
            ret.push_back(ans);
        }
        if (found) {
            for (int i = start + 1; i<s.size(); ++i) {
                p.push_back(i);
                traverse(s, p, i);
                p.pop_back();
            }
        }
    }

    vector<vector<string>> partition(string s) {
        vector<int> p({0});
        dp = vector<vector<int>>(s.size()+1, vector<int>(s.size()+1, -1));
        traverse(s, p, 0);
        return ret;
    }

    void test() {
        vector<vector<string>> ret = partition("aab");
        cout<<"--"<<endl;
        for (auto& v: ret) {
            for (auto& s: v)
                cout<<s<<" ";
            cout<<endl;
        }
    }
};
