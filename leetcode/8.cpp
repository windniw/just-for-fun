class Solution {
public:
    int myAtoi(string str) {
        int k = 0, t=1;
        long long res = 0;
        while (str[k] == ' ') k++;
        if (str[k] == '-' || str[k] == '+'){
            t = str[k] == '+' ? 1 : -1;
            k++;
        }
        if (str[k] > '9' || str[k] < '0') return 0;
        while (str[k] <= '9' && str[k] >= '0' && k<str.size()){
            res = res * 10 + str[k] - '0';
            if (res*t > INT_MAX || res*t < INT_MIN){
                return t == 1 ? INT_MAX : INT_MIN;
            }
            k++;
        }
        return (int)res*t;
    }
};
