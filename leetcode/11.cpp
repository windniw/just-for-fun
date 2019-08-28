class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0, j = height.size()-1;
        int maximum = 0;
        while (i<j){
            int h = min(height[i], height[j]);
            maximum = max(maximum, h*(j-i));
            while (height[i]<=h && i<j) i++;
            while (height[j]<=h && i<j) j--;
        }
        return maximum;
    }
};
