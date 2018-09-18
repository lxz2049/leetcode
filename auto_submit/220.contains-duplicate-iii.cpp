/*
 * [220] Contains Duplicate III
 *
 * https://leetcode.com/problems/contains-duplicate-iii/description/
 *
 * algorithms
 * Medium (18.91%)
 * Total Accepted:    75.7K
 * Total Submissions: 400.2K
 * Testcase Example:  '[1,2,3,1]\n3\n0'
 *
 * Given an array of integers, find out whether there are two distinct indices
 * i and j in the array such that the absolute difference between nums[i] and
 * nums[j] is at most t and the absolute difference between i and j is at most
 * k.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,2,3,1], k = 3, t = 0
 * Output: true
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [1,0,1,1], k = 1, t = 2
 * Output: true
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [1,5,9,1,5,9], k = 2, t = 3
 * Output: false
 * 
 * 
 * 
 * 
 */
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        map<long, long> last;       
        for (int i=0; i<nums.size(); ++i) {
            long cur = nums[i];
            map<long, long>::iterator lo = last.lower_bound(cur);
            if (lo != last.end()) {
                //cout<<"next "<<cur<<" "<<lo->first<<endl;
                if (lo->first - cur <= t) {
                    return true;
                }
            }
            if (lo != last.begin()) {
                lo--;
                //cout<<"prev "<<cur<<" "<<lo->first<<endl;
                if (cur - lo->first <= t) {
                    return true;
                }
            }

            last[cur]++;
            if (i >= k && --last[long(nums[i-k])] == 0) {
                //cout<<"erase "<<nums[i-k]<<endl;
                last.erase(long(nums[i-k]));
            }
        }
        return false;
    }

    void test() {
        //vector<int> v = {1,5,9,1,5,9};
        vector<int> v = {-1,2147483647};
        cout<<containsNearbyAlmostDuplicate(v, 1, 2147483647)<<endl;
    }
};
