class Solution {
public:
    int maxCoins(vector<int>& nums, vector<vector<int>>& dp, int left, int right) {
        if (left + 1 == right)  return 0;
        if (dp[left][right] > 0)   return dp[left][right];
        int ret = 0;
        for (int i=left+1; i<right; ++i) {
            //printf("i:%d left:%d right:%d\n", i, left, right);
            ret = max(ret, nums[i] * nums[left] * nums[right] + 
                      maxCoins(nums, dp, left, i) + maxCoins(nums, dp, i, right));
        }
        dp[left][right] = ret;
        return ret;
    }
    int maxCoins(vector<int>& nums) {
        nums.insert(nums.begin(), 1);
        nums.push_back(1);
        int N = nums.size();
        //for (int i=0; i<N; ++i) cout<<nums[i]<<" "; cout<<endl;
        vector<vector<int>> dp(N, vector<int>(N));
        int ret = maxCoins(nums, dp, 0, N-1);
        //for (int i=0; i<N; ++i) { for (int j=0; j<=N; ++j) { cout<<dp[i][j]<<" "; } cout<<endl; }
        return ret;
    }

    void test() {
        vector<int> v1 = {3,1,5,8};
        cout<<maxCoins(v1)<<endl;
        vector<int> v2 = {3,1,5};
        cout<<maxCoins(v2)<<endl;
        vector<int> v3 = {};
        cout<<maxCoins(v3)<<endl;
        vector<int> v4 = {9};
        cout<<maxCoins(v4)<<endl;
    }
};
