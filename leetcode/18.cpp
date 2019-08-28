class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector <int>> res;
        sort(nums.begin(), nums.end());
        int l = (int)nums.size();
        for (int i=0;i<l-3;i++){
            if (i != 0 && nums[i] == nums[i-1]) continue;
            for (int j=i+1;j<l-2;j++){
                if (j != i+1 && nums[j] == nums[j-1]) continue;
                int t1 = j+1, t2 = l-1, aim = target - nums[i] - nums[j];
                while (t1 < t2){
                    if (nums[t1] + nums[t2] < aim)
                        t1++;
                    else if (nums[t1] + nums[t2] > aim)
                        t2--;
                    else {
                        vector<int> s;
                        s.push_back(nums[i]);
                        s.push_back(nums[j]);
                        s.push_back(nums[t1]);
                        s.push_back(nums[t2]);
                        res.push_back(s);
                        do t1++; while (t1 < t2 && nums[t1] == nums[t1-1]);
                        do t2--; while (t1 < t2 && nums[t2] == nums[t2+1]);
                    }
                }
            }
        }
        return res;
    }
};
