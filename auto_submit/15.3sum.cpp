/*
 * [15] 3Sum
 *
 * https://leetcode.com/problems/3sum/description/
 *
 * algorithms
 * Medium (22.02%)
 * Total Accepted:    378K
 * Total Submissions: 1.7M
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * Given an array nums of n integers, are there elements a, b, c in nums such
 * that a + b + c = 0? Find all unique triplets in the array which gives the
 * sum of zero.
 * 
 * Note:
 * 
 * The solution set must not contain duplicate triplets.
 * 
 * Example:
 * 
 * 
 * Given array nums = [-1, 0, 1, 2, -1, -4],
 * 
 * A solution set is:
 * [
 * ⁠ [-1, 0, 1],
 * ⁠ [-1, -1, 2]
 * ]
 * 
 * 
 */
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        unordered_map<int, int> hashmap;
        for (int i=0; i<nums.size(); i++) {
            hashmap[-nums[i]] = i;
        }

        vector<vector<int>> ret;
        for (int i=0; i<nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i-1])
                continue;

            for (int j=i+1; j<nums.size(); j++) {
                if (j > (i+1) && nums[j] == nums[j-1])
                    continue;

                int sum = nums[i] + nums[j];
                if (hashmap[sum] > j) {
                    ret.push_back({nums[i], nums[j], -sum});                   
                }
            }
        }
        return ret;
    }
};
