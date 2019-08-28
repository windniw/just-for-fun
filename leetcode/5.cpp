class Solution {
public:
    string longestPalindrome(string s) {
        int maximum = 1, st = 0;
        for (int i=0;i<s.size()-1;++i){
            check(s, maximum, st, i,i);
            check(s, maximum, st, i,i+1);
        }
        return s.substr(st, maximum);
    }
    void check(string& s, int& maximum, int &st, int i, int j){
        int len = i == j ? -1 : 0, t = j;
        while (i > -1 && j < s.size()){
            if (s[i] == s[j]){
                len += 2;
                i--;
                j++;
            }
            else break;
        }
        if (len > maximum){
            maximum = len;
            st = t-len/2;
        }
    }
};
