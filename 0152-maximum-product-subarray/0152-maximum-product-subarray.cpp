class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        int currProduct = 1;
        int ans = INT_MIN;
        for(int i = 0; i < n; i++) {
            if(nums[i] == 0) {
                ans = max(ans, 0);
                currProduct = 1;
            } else {
                currProduct *= nums[i];
                ans = max(ans, currProduct);
            }
        }

        reverse(nums.begin(), nums.end());
        currProduct = 1;

        for(int i = 0; i < n; i++) {
            if(nums[i] == 0) {
                ans = max(ans, 0);
                currProduct = 1;
            } else {
                currProduct *= nums[i];
                ans = max(ans, currProduct);
            }
        }
        return ans;
    }
};