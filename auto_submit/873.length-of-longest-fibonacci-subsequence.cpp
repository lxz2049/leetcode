/*
 * [905] Length of Longest Fibonacci Subsequence
 *
 * https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/
 *
 * algorithms
 * Medium (42.20%)
 * Total Accepted:    6.8K
 * Total Submissions: 16K
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
 * 
 */
class Solution {
public:
    int lenLongestFibSubseq(vector<int>& A) {
        int ret = 0;
        unordered_set<int> s(A.begin(), A.end());
        for (int i=0; i<A.size()-2; ++i) {
            if (A.size()-1-i+1 <= ret)
                break;
            for (int j=i+1; j<A.size()-1; ++j) {
                if (A.size()-1-j <= ret)
                    break;
                int prev = A[i];
                int cur = A[j];
                int len = 0;
                while (s.find(prev + cur) != s.end()) {
                    int tmp = prev + cur;
                    prev = cur;
                    cur = tmp;
                    len ++;
                }
                ret = max(len, ret);
            }
        }

        return ret > 0 ? ret + 2 : 0;
    }

    void test() {
        vector<int> v = {1,2,3,4,5,6,7,8};
        cout<<lenLongestFibSubseq(v)<<endl;
        vector<int> v1 = {1,3,7,11,12,14,18};
        cout<<lenLongestFibSubseq(v1)<<endl;
        vector<int> v2 = {1,3};
        cout<<lenLongestFibSubseq(v2)<<endl;
    }
};
