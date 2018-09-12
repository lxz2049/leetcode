/*
 * [238] Product of Array Except Self
 *
 * https://leetcode.com/problems/product-of-array-except-self/description/
 *
 * algorithms
 * Medium (51.46%)
 * Total Accepted:    176.8K
 * Total Submissions: 343K
 * Testcase Example:  '[1,2,3,4]'
 *
 * Given an array nums of n integers where n > 1,  return an array output such
 * that output[i] is equal to the product of all the elements of nums except
 * nums[i].
 * 
 * Example:
 * 
 * 
 * Input:  [1,2,3,4]
 * Output: [24,12,8,6]
 * 
 * 
 * Note: Please solve it without division and in O(n).
 * 
 * Follow up:
 * Could you solve it with constant space complexity? (The output array does
 * not count as extra space for the purpose of space complexity analysis.)
 * 
 */
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans = nums;
        for (int i=1; i<ans.size(); ++i) {
            ans[i] *= ans[i-1];
        }

        int runningProd = 1;
        for (int i=ans.size()-1; i >0; --i) {
            ans[i] = ans[i-1] * runningProd;
            runningProd *= nums[i];
        }
        ans[0] = runningProd;
        return ans;
    }

    void test() {
        vector<int> nums = {1,2,3,4};
        vector<int> ret = productExceptSelf(nums);
        //printVector(ret);
    }
};
