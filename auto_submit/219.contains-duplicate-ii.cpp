/*
 * [219] Contains Duplicate II
 *
 * https://leetcode.com/problems/contains-duplicate-ii/description/
 *
 * algorithms
 * Easy (33.48%)
 * Total Accepted:    161.2K
 * Total Submissions: 480.2K
 * Testcase Example:  '[1,2,3,1]\n3'
 *
 * Given an array of integers and an integer k, find out whether there are two
 * distinct indices i and j in the array such that nums[i] = nums[j] and the
 * absolute difference between i and j is at most k.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,2,3,1], k = 3
 * Output: true
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [1,0,1,1], k = 1
 * Output: true
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [1,2,3,1,2,3], k = 2
 * Output: false
 * 
 * 
 * 
 * 
 */
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if (nums.size() == 0)   return false;
        unordered_map<int, int> lastAppearance;       
        for (int i=0; i<nums.size(); ++i) {
            if (lastAppearance.find(nums[i]) == lastAppearance.end() ||
                i - lastAppearance[nums[i]] > k) {
                lastAppearance[nums[i]] = i;
            } else {
                return true;
            }
        }
        return false;
    }

    void test() {
        vector<int> nums = {1,2,3,1,2,3};
        cout<<containsNearbyDuplicate(nums, 2)<<endl;
    }
};
