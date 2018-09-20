/*
 * [52] N-Queens II
 *
 * https://leetcode.com/problems/n-queens-ii/description/
 *
 * algorithms
 * Hard (48.37%)
 * Total Accepted:    83K
 * Total Submissions: 170.8K
 * Testcase Example:  '4'
 *
 * The n-queens puzzle is the problem of placing n queens on an n×n chessboard
 * such that no two queens attack each other.
 * 
 * 
 * 
 * Given an integer n, return the number of distinct solutions to the n-queens
 * puzzle.
 * 
 * Example:
 * 
 * 
 * Input: 4
 * Output: 2
 * Explanation: There are two distinct solutions to the 4-queens puzzle as
 * shown below.
 * [
 * [".Q..",  // Solution 1
 * "...Q",
 * "Q...",
 * "..Q."],
 * 
 * ["..Q.",  // Solution 2
 * "Q...",
 * "...Q",
 * ".Q.."]
 * ]
 * 
 * 
 */
class Solution {
public:
    void shiftLeft(vector<int>& v, int j) {
        for (int i=0; i<v.size()-1; ++i) {
            v[i] = v[i+1];
        }
        v[v.size()-1] = 0;
        if (j > 0) v[j-1] = 1;
    }
    void shiftRight(vector<int>& v, int j) {
        for (int i=v.size()-1; i>0; --i) {
            v[i] = v[i-1];
        }
        v[0] = 0;
        if (j < v.size()-1) v[j+1] = 1;
    }
    int traverse(vector<int>& up, vector<int>& left, vector<int>& right, int l, int n) {
        if (l >= n)   return 1;
        int ret = 0;
        for (int i=0; i<n; ++i) {
            if (!up[i] && !left[i] && !right[i]) {
                up[i] = 1;
                vector<int> leftcopy = left;
                vector<int> rightcopy = right;
                shiftLeft(left, i);
                shiftRight(right, i);
                ret += traverse(up, left, right, l+1, n);
                up[i] = 0;
                left = leftcopy;
                right = rightcopy;
            }
        }       
        return ret;
    }

    int totalNQueens(int n) {
        vector<int> up(n);
        vector<int> left(n);
        vector<int> right(n);
        return traverse(up, left, right, 0, n);
    }

    void test() {
        cout<<totalNQueens(5)<<endl;
    }
};
