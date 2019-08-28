class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        if (x < 10) return true;
        if (x%10==0) return false;
        int t = 0;
        while (t < x){
            t = t * 10 + x % 10;
            if (x == t) return true;
            x = x / 10;
            if (x == t) return true;
        }
        return false;
    }
};
