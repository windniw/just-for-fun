class Solution {
public:
    int getKth(vector<int>& A, int st_A, vector<int>& B, int st_B, int k){
    if (st_A == A.size())
        return B[st_B + k-1];
    else if (st_B == B.size())
        return A[st_A + k-1];
    else if (k == 1)
        return min(A[st_A], B[st_B]);
    
    int a = min((int)A.size() - st_A, k >> 1);
    int b = min((int)B.size() - st_B, k >> 1);
    if (A[a + st_A - 1] <= B[b + st_B - 1])
        return getKth(A, a + st_A, B, st_B, k - a);
    else
        return getKth(A, st_A, B, b + st_B, k - b);
    }

    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int sum = nums1.size() + nums2.size();
        return (getKth(nums1, 0, nums2, 0, (sum >> 1) + 1) + getKth(nums1, 0, nums2, 0, sum - (sum >> 1))) / 2.0;
    }

};
