/*
 * [45] Jump Game II
 *
 * https://leetcode.com/problems/jump-game-ii/description/
 *
 * algorithms
 * Hard (26.16%)
 * Total Accepted:    109.4K
 * Total Submissions: 418K
 * Testcase Example:  '[0]'
 *
 * 
 * Given an array of non-negative integers, you are initially positioned at the
 * first index of the array.
 * 
 * 
 * Each element in the array represents your maximum jump length at that
 * position. 
 * 
 * 
 * Your goal is to reach the last index in the minimum number of jumps.
 * 
 * 
 * 
 * For example:
 * Given array A = [2,3,1,1,4]
 * 
 * 
 * The minimum number of jumps to reach the last index is 2. (Jump 1 step from
 * index 0 to 1, then 3 steps to the last index.)
 * 
 * 
 * 
 * Note:
 * You can assume that you can always reach the last index.
 */
class Solution {
public:
    int jump(vector<int>& nums) {
		int size = nums.size();
		int start = 0, end = 1, jumps = 0;
 		for (int i=0, j=1; i<size, j<size; ++i) {
			if (i>=end) {
				start = i;
				end = j;
				jumps ++;
				//printf("start:%d end:%d jumps:%d\n", start, end, jumps);
			}
			while (j<min(size, i+nums[i]+1)) {
				j++;
			}
		}

		if (size > end)
			jumps++;
		return jumps;
    }

	bool test() {
		int a[] = {2, 3, 1, 1, 4};
		vector<int> v(a, a+5);
		return jump(v) == 2;
	}
};
