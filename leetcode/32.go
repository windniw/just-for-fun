/*

link: https://leetcode.com/problems/longest-valid-parentheses

problem: 求括号串的最长合法子串长度

solution: 正常出入栈即可，考虑异常场景，只有多余的'('已及')'; 多余的')'代表着前面的子串绝对不可能和后面子串连起来,
          而多余的'('只可能存在最后一段；如这个串，(())) | (()()(()，视为两段考虑即可，后半段计算栈中剩余的'('的
          间隔，即可知中间的合法序列长度

solution-fix: 啊这特么居然是个dp...定义dp[i]为以s[i]结尾的最长合法子串长度；处理下边界条件正常转移即可

solution-fix-fix: 
从左往右，记L='('出现的次数，记R=')'出现的次数
- if R>L L=0,R=0 清零计数器，因为后面的'('不可能匹配左侧的')'
- if R=L 当前左侧为一个合法串（不合法的都清零了），更新最大值
再从右往左对称来一遍即可

前两个空间复杂都都是O(n)，这个降到了O(1)；一开始就这个搞法然而想到没有逆序一下就可以处理(()的情况

*/

type stack struct {
	buff []int
	p    int
}

func (s *stack) pop() int {
	s.p--
	return s.buff[s.p+1]
}

func (s *stack) empty() bool {
	return s.p == -1
}

func (s *stack) push(c int) {
	s.p++
	s.buff[s.p] = c
}

func (s *stack) clear() {
	s.p = -1
}

func longestValidParentheses(s string) int {
	st := stack{
		buff: make([]int, len(s)),
		p:    -1,
	}
	cur, res := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			st.push(i)
		} else {
			if !st.empty() {
				st.pop()
				cur += 2
				if st.empty() && cur > res {
					res = cur
				}
			} else {
				st.clear()
				if cur > res {
					res = cur
				}
				cur = 0
			}
		}
	}
	if !st.empty() {
		c := len(s)
		for !st.empty() {
			cc := st.pop()
			if c-cc-1 > res {
				res = c - cc - 1
			}
			c = cc
		}
	} else {
		if cur > res {
			res = cur
		}
	}
	return res
}

// ---
func longestValidParentheses(s string) int {
	res := 0
	dp := make([]int, len(s))
	f := func(i, n int) {
		dp[i] = n
		if n > res {
			res = n
		}
	}
	g := func(i int) int {
		if i >= 0 {
			return dp[i]
		} else {
			return 0
		}
	}
	for i := 1; i < len(s); i++ {
		switch s[i] {
		case '(':
			f(i, 0)
		case ')':
			if s[i-1] == '(' {
				f(i, g(i-2)+2)
			} else {
				if i-1-dp[i-1] >= 0 && s[i-1-dp[i-1]] == '(' {
					f(i, g(i-1-dp[i-1]-1)+g(i-1)+2)
				} else {
					f(i, 0)
				}
			}
		}
	}
	return res
}

// ---
func longestValidParentheses(s string) int {
	l, r, res := 0, 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			l++
		} else {
			r++
		}
		if l < r {
			l, r = 0, 0
		} else if l == r {
			if l+r > res {
				res = l + r
			}
		}
	}
	l, r = 0, 0
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == '(' {
			l++
		} else {
			r++A
		}
		if l > r {
			l, r = 0, 0
		} else if l == r {
			if l+r > res {
				res = l + r
			}
		}
	}
	return res
}
