/*
 * [132] Palindrome Partitioning II
 *
 * https://leetcode.com/problems/palindrome-partitioning-ii/description/
 *
 * algorithms
 * Hard (25.57%)
 * Total Accepted:    89.1K
 * Total Submissions: 346.2K
 * Testcase Example:  '"aab"'
 *
 * Given a string s, partition s such that every substring of the partition is
 * a palindrome.
 * 
 * Return the minimum cuts needed for a palindrome partitioning of s.
 * 
 * Example:
 * 
 * 
 * Input: "aab"
 * Output: 1
 * Explanation: The palindrome partitioning ["aa","b"] could be produced using
 * 1 cut.
 * 
 * 
 */
class Solution {
public:
    bool isPalin(string &s, vector<vector<int>> &dp, int i, int j) {
        if (i >= j) return true;
        return s[i] == s[j] && (i == j-1 || dp[i+1][j-1] == 0);
    }
    int minCut(string s) {
        vector<vector<int>> dp(s.size(), vector<int>(s.size(), 1));
        dp[0][0] = 0;
        for (int i=1; i<s.size(); ++i) {
            int mincut = s.size();
            for (int j=0; j<=i; ++j) {
                if (isPalin(s, dp, j, i)) {
                    //cout<<j<<i<<s.substr(j, i-j+1)<<endl;
                    dp[j][i] = 0;
                    mincut = j == 0 ? 0: min(mincut, dp[0][j-1] + 1);
                }
            }
            dp[0][i] = mincut;
        }
        //for (int i=0; i<s.size(); ++i) {for (int j=0; j<s.size(); ++j) cout<<dp[i][j]<<" "; cout<<endl;}
        return dp[0][s.size()-1];
    }
    void test() {
        cout<<minCut("aab")<<endl;
        cout<<minCut("cabababcbc")<<endl;
        cout<<minCut("cbbbcc")<<endl;
        cout<<minCut("fff")<<endl;
    }
};
