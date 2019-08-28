class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;
        string res = "";
        for (int i=0;i<numRows;++i){
            int k = i;
            while (k < s.size()){
                res += s[k];
                if (i != 0 && i != numRows-1){
                    k+=2*(numRows-1-i);
                    if (k < s.size()) res += s[k];
                    k+=2*i;
                }
                else 
                    k += 2*numRows-2;
            }
        }
        return res;
    }
};
