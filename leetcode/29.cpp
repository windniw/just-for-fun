/*

link: https://leetcode.com/problems/divide-two-integers

problem: 禁用 * / % , 求整数除法，限定在[-2^31, 2^31-1]间，溢出返回 2^31-1

solution: 反复左移除数找到该位的最大值，然后用被除数减去该值，递归即可；即通过快速减法的方式去做除法

solution-fix: 题目隐含限制了不能使用 long long，在 int 模式下需要特殊处理的是，要将入参转为负数而不能是整数，abs(INT_MIN) > INT_MAX，在此时会值溢出

*/

class Solution {
public:
    int divide(int dividend, int divisor) {
        long long dividend_in = dividend, divisor_in = divisor;
        if (dividend_in == -(1ll<<31) && (divisor_in == -1)) {
            return (1ll << 31) -1;
        }
        long long res = 0;
        int r = (dividend_in < 0) ^ (divisor_in < 0);
        dividend_in = abs(dividend_in);
        divisor_in = abs(divisor_in);
        while (dividend_in >= divisor_in) {
            int n = 1;
            while ((divisor_in << n) < dividend_in) {
                n += 1;
            }
            res += (1ll << (n - 1));
            dividend_in -= (divisor_in << (n - 1));
        }
        return !r ? res : -res;
    }
};

// ---
class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }
        if (divisor == 1) {
            return dividend;
        }

        int r = (dividend < 0) ^ (divisor < 0);
        dividend = dividend > 0 ? -dividend : dividend;
        divisor = divisor > 0 ? -divisor : divisor;

        int res = 0;

        while (dividend <= divisor) {
            int n = 0;
            int c = divisor;
            while (dividend - c < c) {
                n += 1;
                c += c;
            }
            res += 1 << n;
            dividend -= c;
        }
        return !r ? res : -res;
    }
};
