class RLEIterator {
private:
    vector<int> nums;
    int idx;
public:
    RLEIterator(vector<int> A) {
        nums = A;
        idx = 0;
    }
    
    int next(int n) {
        int ret = -1;
        while (n && idx < nums.size()) {
            if (n >= nums[idx]) {
                n -= nums[idx];
                ret = nums[idx+1];
                idx += 2;
            } else {
                nums[idx] -= n;
                ret = nums[idx+1];
                n = 0;
            }
        }
        if (n)  return -1;
        return ret;
    }
};

/**
 * Your RLEIterator object will be instantiated and called as such:
 * RLEIterator obj = new RLEIterator(A);
 * int param_1 = obj.next(n);
 */

class Solution {
public:
    void test() {
        vector<int> nums = {3,8,0,9,2,5};
        RLEIterator iter(nums);
        cout<<iter.next(2)<<endl;
        cout<<iter.next(1)<<endl;
        cout<<iter.next(1)<<endl;
        cout<<iter.next(2)<<endl;
        cout<<iter.next(1)<<endl;
    }
};
