class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> v;
        dfs(v, "", n*2, 0, 0);
        return v;
    }
    
    void dfs(vector<string>& v, string cur, int n, int k, int lb){
        if (k == n){
            v.push_back(cur);
        }
        if (lb < n-k) dfs(v, cur+"(", n, k+1, lb+1);
        if (lb != 0) dfs(v, cur+")", n, k+1, lb-1);
    }
};

