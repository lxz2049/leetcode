/*
 * [329] Longest Increasing Path in a Matrix
 *
 * https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
 *
 * algorithms
 * Hard (37.74%)
 * Total Accepted:    61.8K
 * Total Submissions: 163.6K
 * Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
 *
 * Given an integer matrix, find the length of the longest increasing path.
 * 
 * From each cell, you can either move to four directions: left, right, up or
 * down. You may NOT move diagonally or move outside of the boundary (i.e.
 * wrap-around is not allowed).
 * 
 * Example 1:
 * 
 * 
 * Input: nums = 
 * [
 *   [9,9,4],
 *   [6,6,8],
 *   [2,1,1]
 * ] 
 * Output: 4 
 * Explanation: The longest increasing path is [1, 2, 6, 9].
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = 
 * [
 *   [3,4,5],
 *   [3,2,6],
 *   [2,2,1]
 * ] 
 * Output: 4 
 * Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
 * is not allowed.
 * 
 * 
 */
class Solution {
public:
    int traverse(vector<vector<int>>& matrix, vector<vector<int>>& dp, int i, int j) {
       if (i < 0 || j < 0 || i >= matrix.size() || j >= matrix[i].size()) return 0; 
       if (dp[i][j]) return dp[i][j];
       //cout<<i<<" "<<j<<endl;
       if (i+1 < matrix.size() && matrix[i+1][j] > matrix[i][j]) {
           dp[i][j] = max(dp[i][j], traverse(matrix, dp, i+1, j));
       }
       if (i-1 >= 0 && matrix[i-1][j] > matrix[i][j]) {
           dp[i][j] = max(dp[i][j], traverse(matrix, dp, i-1, j));
       }
       if (j+1 < matrix[0].size() && matrix[i][j+1] > matrix[i][j]) {
           dp[i][j] = max(dp[i][j], traverse(matrix, dp, i, j+1));
       }
       if (j-1 >= 0 && matrix[i][j-1] > matrix[i][j]) {
           dp[i][j] = max(dp[i][j], traverse(matrix, dp, i, j-1));
       }
       dp[i][j] ++;
       return dp[i][j];
    }
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if (!matrix.size()) return 0;
        vector<vector<int>> dp(matrix.size(), vector<int>(matrix[0].size()));
        int ret = 0;
        for (int i=0; i<matrix.size(); ++i) {
            for (int j=0; j<matrix[i].size(); ++j) {
                ret = max(ret, traverse(matrix, dp, i, j));
            }
        }
        return ret;
    }

    void test() {
        vector<int> a = {3,4,5};
        vector<int> b = {3,2,6};
        vector<int> c = {2,2,1};
        vector<vector<int>> matrix;
        matrix.push_back(a);
        matrix.push_back(b);
        matrix.push_back(c);
        cout<<longestIncreasingPath(matrix)<<endl;
    }
};
