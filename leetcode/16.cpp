class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int res = nums[0] + nums[1] + nums[2];
        for (int i=0; i<nums.size(); ++i){
            int l = i + 1, r = nums.size() - 1;
            while (l < r){
                int t = nums[i] + nums[l] + nums[r];
                if (abs(target - t) < abs(target - res))
                    res = t;
                if (t < target) l++;
                else r--;
                if (res == target) return res;
            }
        }
        return res;
    }
};
