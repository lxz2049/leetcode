/*
 * [300] Longest Increasing Subsequence
 *
 * https://leetcode.com/problems/longest-increasing-subsequence/description/
 *
 * algorithms
 * Medium (38.86%)
 * Total Accepted:    113.5K
 * Total Submissions: 292.1K
 * Testcase Example:  '[10,9,2,5,3,7,101,18]'
 *
 * 
 * Given an unsorted array of integers, find the length of longest increasing
 * subsequence.
 * 
 * 
 * For example,
 * Given [10, 9, 2, 5, 3, 7, 101, 18],
 * The longest increasing subsequence is [2, 3, 7, 101], therefore the length
 * is 4. Note that there may be more than one LIS combination, it is only
 * necessary for you to return the length.
 * 
 * 
 * Your algorithm should run in O(n2) complexity.
 * 
 * 
 * Follow up: Could you improve it to O(n log n) time complexity? 
 * 
 * Credits:Special thanks to @pbrother for adding this problem and creating all
 * test cases.
 */
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int size = nums.size();
        vector<int> LISlen(size, 1);
        for (int i=size-1; i>=0; --i) {
            //printf("\nnums[i]:%d\n", nums[i]);
            for (int j=i+1; j<size; ++j) {
                if (nums[j] > nums[i]) {
                    //printf("nums[j]:%d LISlen[j]:%d\n", nums[j], LISlen[j]);
                    LISlen[i] = max(LISlen[i], LISlen[j] + 1);
                }
            }
        }
        int ans = 0;
        for (int i=0; i<size; ++i) {
            //printf("nums[i]:%d LISlen[i]:%d\n", nums[i], LISlen[i]);
            ans = max(ans, LISlen[i]);
        }
        return ans;
    }

    bool test() {
        int a[] = {10, 9, 2, 5, 3, 7, 101, 18};
        //int a[] = {10, 9, 2, 5, 3, 4};
        vector<int> v(a, a+sizeof(a)/sizeof(int));
        return lengthOfLIS(v) == 4;
    }
};
