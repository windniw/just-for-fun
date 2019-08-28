class Solution {
public:
    void getP(string& p, int k, char& match, bool& sign){
        sign = false;
        match = p[k];
        if (k<p.size()-1 && p[k+1] == '*') sign = true;
    }
    bool isMatch(string s, string p) {
        vector<vector<bool> > f(s.size()+1, vector<bool>(p.size()+1, false));
        char match;bool sign;
        f[0][0] = true;
        for (int i=0;i<=p.size();++i) {
            if (p[i] == '*') {f[0][i+1] = f[0][i];continue;}
            getP(p,i,match,sign);
            f[0][i+1] = f[0][i] && sign;
        }
        for (int i=0;i<s.size();++i){
            for (int j=0;j<p.size();++j){
                if (p[j] == '*') {f[i+1][j+1] = f[i+1][j];continue;}
                getP(p, j, match, sign);
                f[i+1][j+1] = ((match == '.' || match == s[i]) && f[i][j]) || (sign && f[i+1][j]) || (sign && (match == '.' || match == s[i]) && f[i][j+1]);
            }
        }
        return f[s.size()][p.size()];
    }

};
