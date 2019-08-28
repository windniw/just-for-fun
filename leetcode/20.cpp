class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        int l = s.length();
        for (int i=0;i<l;++i){
            if (s[i] == '(' || s[i] == '{' || s[i] == '[')
                st.push(s[i]);
            else {
                if (st.empty()) return false;
                char t = st.top();
                if (t != s[i]-1 && t != s[i]-2) return false;
                st.pop();
            }
        }
        return st.empty();
    }
};
