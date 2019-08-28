/*

link: https://leetcode.com/problems/divide-two-integers

problem: 禁用 * / % , 求整数除法，限定在[-2^31, 2^31-1]间，溢出返回 2^31-1

solution: 反复左移除数找到该位的最大值，然后用被除数减去该值，递归即可；即通过快速减法的方式去做除法

*/

func divide(dividend int, divisor int) int {
	factor := 1

	if (dividend > 0 && divisor < 0) || (dividend < 0 && divisor > 0) {
		factor = -1
	}
	if dividend < 0 {
		dividend = -dividend
	}
	if divisor < 0 {
		divisor = -divisor
	}
	var n uint = 31
	for n >= 0 {
		if dividend >= divisor<<n {
			res := (1<<n + divide(dividend-divisor<<n, divisor)) * factor
			if res > (1<<31)-1 || res < -(1<<31) {
				return 1<<31 - 1
			} else {
				return res
			}
		}
		if n == 0 {
			break
		}
		n--
	}
	return 0
}