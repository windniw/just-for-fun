class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        for (int i=0;i<n;++i){
            if (i!=0 && nums[i] == nums[i-1]) continue;
            int l = i+1, r = n-1;
            while (l<r){
                if (nums[l]+nums[r] == -nums[i]){
                    vector<int> t;
                    t.push_back(nums[i]);t.push_back(nums[l]);t.push_back(nums[r]);
                    res.push_back(t);
                    while (nums[l] == nums[l+1] && l<r) l++;
                    while (r!=n-1 && nums[r-1] == nums[r] && l<r) r--;
                }
                if (nums[l]+nums[r] <= -nums[i]) l++;
                else r--;
            }
        }
        return res;
    }
};
