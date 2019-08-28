class Solution {
public:
    string compare(string s1, string s2){
        int len = min(s1.size(), s2.size()), k=0;
        for (;k<len;++k){
            if (s1[k] != s2[k]) break;
        }
        return s1.substr(0,k);
    }
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0) return "";
        if (strs.size() == 1) return strs[0];
        string t = compare(strs[0], strs[1]);
        for (int i=2;i<strs.size();++i){
            t = compare(t, strs[i]);
        }
        return t;
    }
};
