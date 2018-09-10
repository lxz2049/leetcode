/*
 * [905] Length of Longest Fibonacci Subsequence
 *
 * https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/
 *
 * algorithms
 * Medium (41.04%)
 * Total Accepted:    5.2K
 * Total Submissions: 12.7K
 * Testcase Example:  '[1,2,3,4,5,6,7,8]'
 *
 * A sequence X_1, X_2, ..., X_n is fibonacci-like if:
 * 
 * 
 * n >= 3
 * X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
 * 
 * 
 * Given a strictly increasing array A of positive integers forming a sequence,
 * find the length of the longest fibonacci-like subsequence of A.  If one does
 * not exist, return 0.
 * 
 * (Recall that a subsequence is derived from another sequence A by deleting
 * any number of elements (including none) from A, without changing the order
 * of the remaining elements.  For example, [3, 5, 8] is a subsequence of [3,
 * 4, 5, 6, 7, 8].)
 * 
 * 
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: [1,2,3,4,5,6,7,8]
 * Output: 5
 * Explanation:
 * The longest subsequence that is fibonacci-like: [1,2,3,5,8].
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: [1,3,7,11,12,14,18]
 * Output: 3
 * Explanation:
 * The longest subsequence that is fibonacci-like:
 * [1,11,12], [3,11,14] or [7,11,18].
 * 
 * 
 * 
 * 
 * Note:
 * 
 * 
 * 3 <= A.length <= 1000
 * 1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
 * (The time limit has been reduced by 50% for submissions in Java, C, and
 * C++.)
 * 
 */
class Solution {
public:
    int lenLongestFibSubseq(vector<int>& nums) {
        vector<vector<int>> dp(nums.size(), vector<int>(nums.size(), 0));
        unordered_map<int, int> m;
        for (int i=0; i<nums.size(); ++i)
            m[nums[i]] = i;

        int maxSeqLen = 0;
        for (int i=0; i<nums.size(); ++i) {
            for (int j=i+1; j<nums.size(); ++j) {
                if (!dp[i][j]) {
                    int prev = nums[i];
                    int cur = nums[j];
                    vector<int> seq = {i, j};
                    while (m.find(prev+cur) != m.end()) {
                        seq.push_back(m[prev+cur]);
                        cur = prev + cur;
                        prev = cur - prev;
                    }
                    for (int k=0; k<seq.size()-1; ++k) {
                        dp[seq[k]][seq[k+1]] = seq.size();
                    }
                    maxSeqLen = max(maxSeqLen, int(seq.size()));
                }
            }
        }
        return maxSeqLen > 2 ? maxSeqLen: 0;
    }
};
