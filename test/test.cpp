#include <stdio.h>
#include <vector>

#include "42.trapping-rain-water.cpp"

using namespace std;

int main() {
	Solution s = Solution();
	int nums_array[12] = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
	//int nums_array[6] = {5, 2, 1, 2, 1, 5};
	vector<int> nums(nums_array, nums_array + sizeof(nums_array) / sizeof(int));
	printf("%d\n", s.trap(nums));

	return 0;
}
