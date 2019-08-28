class Solution {
public:
    const char m[10][5] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        joint(digits, 0, "", res);
        return res;
    }
private:
    void joint(string str, int k, string cur, vector<string> &res){
        if (k >= str.size()){
            if (cur != "")
                res.push_back(cur);
            return;
        }
        int len = strlen(m[str[k]-'0']);
        for (int i=0;i<len;++i){
            joint(str, k+1, cur + m[str[k]-'0'][i], res);
        }
    }
};
