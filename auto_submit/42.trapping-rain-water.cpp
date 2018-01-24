class Solution {
public:
    int trap(vector<int>& height) {
		vector<int> new_height(height);
		int size = height.size();
		for (int i = 1; i < size-1; ++i) {
			if (left(new_height, i) && right(new_height, i)) {
				//printf("found low point %d\n", i);
				int l=i;
				int r=i;
				while (left(new_height, l)) {
					l--;
				}
				while (right(new_height, r)) {
					r++;
				}
				//printf("expanded left to %d\n", l);
				//printf("expanded right to %d\n", r);
				int low = new_height[i];
				int high = new_height[l] < new_height[r] ? new_height[l] : new_height[r];
				for (int j = l+1; j < r; j++) {
					new_height[j] = new_height[j] < high ? high : new_height[j];
				}
			}
		}

		// debug
		for (int i = 1; i < size-1; ++i) {
			//printf("%d ", new_height[i]);
		}
		//printf("\n");
		// debug

		int volumn = 0;
		for (int i = 1; i < size-1; ++i) {
			volumn += new_height[i] - height[i] > 0 ? new_height[i] - height[i] : 0;
		}
		return volumn;
    }

	bool left(vector<int>& height, int l) {
		return height[l-1] >= height[l] && l-1 >= 0;
	}

	bool right(vector<int>& height, int r) {
		return height[r+1] >= height[r] && r+1 < height.size();
	}

};
