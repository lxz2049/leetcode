//#include <vector>
//using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
		int i;
 		for (i = 0; i < nums.size(); ++i) {
			int index = nums[i] - 1;
			while (nums[i] > 0 && index < nums.size() && nums[i] != nums[index]) {
				//printf("swapping %d with %d\n", nums[i], nums[index]);
				swap(nums[i], nums[index]);
				index = nums[i] - 1;
			}
		}

		// DEBUG
 		//for (int i = 0; i < nums.size(); ++i) {
		//	printf("%d ", nums[i]);
		//}
		//printf("\n");
		//DEBUG END

 		for (i = 0; i < nums.size(); ++i) {
			if (nums[i] != i+1) { 
				break;
			}
		}

		return i+1;
    }

	void swap(int &a, int &b) {
		int tmp = a;
		a = b;
		b = tmp;
	}
};
