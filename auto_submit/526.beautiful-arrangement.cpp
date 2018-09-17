/*
 * [526] Beautiful Arrangement
 *
 * https://leetcode.com/problems/beautiful-arrangement/description/
 *
 * algorithms
 * Medium (52.99%)
 * Total Accepted:    28.5K
 * Total Submissions: 53.8K
 * Testcase Example:  '2'
 *
 * 
 * Suppose you have N integers from 1 to N. We define a beautiful arrangement
 * as an array that is constructed by these N numbers successfully if one of
 * the following is true for the ith position (1 
 * The number at the ith position is divisible by i.
 * i is divisible by the number at the ith position.
 * 
 * 
 * 
 * 
 * Now given N, how many beautiful arrangements can you construct?
 * 
 * 
 * Example 1:
 * 
 * Input: 2
 * Output: 2
 * Explanation: 
 * The first beautiful arrangement is [1, 2]:
 * Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
 * Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
 * The second beautiful arrangement is [2, 1]:
 * Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
 * Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
 * 
 * 
 * 
 * Note:
 * 
 * N is a positive integer and will not exceed 15.
 * 
 * 
 */
class Solution {
public:
    int traverse(vector<bool> &used, int n, int N) {
        if (n == N + 1) return 1;
        int ret = 0;
        for (int i=1; i<used.size(); ++i) {
            if (!used[i] && (i % n == 0 || n % i == 0)) {
                used[i] = true;
                ret += traverse(used, n+1, N);
                used[i] = false;
            }
        }
        return ret;
    }

    int countArrangement(int N) {
        vector<bool> used(N+1);
        return traverse(used, 1, N);
    }

    void test() {
        cout<<countArrangement(3)<<endl;
        cout<<countArrangement(4)<<endl;
    }
};
