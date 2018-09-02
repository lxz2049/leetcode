/*
 * [128] Longest Consecutive Sequence
 *
 * https://leetcode.com/problems/longest-consecutive-sequence/description/
 *
 * algorithms
 * Hard (38.50%)
 * Total Accepted:    157.7K
 * Total Submissions: 402.6K
 * Testcase Example:  '[100,4,200,1,3,2]'
 *
 * Given an unsorted array of integers, find the length of the longest
 * consecutive elements sequence.
 * 
 * Your algorithm should run in O(n) complexity.
 * 
 * Example:
 * 
 * 
 * Input: [100, 4, 200, 1, 3, 2]
 * Output: 4
 * Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
 * Therefore its length is 4.
 * 
 * 
 */
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s;
        for (int i = 0; i < nums.size(); ++i) {
            s.insert(nums[i]);
        }       

        int ans = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (s.find(nums[i]-1) == s.end()) {
                int start = nums[i];
                int size = 1;
                while (s.find(start+1) != s.end()) {
                    start ++;
                    size ++;
                }
                ans = max(ans, size);
            }
                
        }
        return ans;
    }

    void test() {
        int a[] = {100,4,200,1,3,2};
        vector<int> v(a, a+6);
        cout<<longestConsecutive(v)<<endl;
    }
};
