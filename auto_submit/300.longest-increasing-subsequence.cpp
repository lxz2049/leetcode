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
        vector<int> listLen;
		for (int i=0; i<size; ++i) {
			vector<int>::iterator j = lower_bound(listLen.begin(), listLen.end(), nums[i]);
			if (j == listLen.end()) {
				listLen.push_back(nums[i]);
			} else {
				*j = nums[i];
			}
		}
        return listLen.size();
    }

    bool test() {
        int a[] = {10, 9, 2, 5, 3, 7, 101, 18};
        //int a[] = {10, 9, 2, 5, 3, 4};
        vector<int> v(a, a+sizeof(a)/sizeof(int));
        return lengthOfLIS(v) == 4;
    }
};

