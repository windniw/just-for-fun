class Solution {
public:
    string intToRoman(int num) {
        string arr[] ={"","I","II","III","IV","V","VI","VII","VIII","IX",
                       "","X","XX","XXX","XL","L","LX","LXX","LXXX","XC",
                       "","C","CC","CCC","CD","D","DC","DCC","DCCC","CM",
                       "","M","MM","MMM"};
        return arr[30+num/1000]+arr[20+num%1000/100]+arr[10+num%100/10]+arr[num%10];
    }
};
