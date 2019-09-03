/*

link: https://leetcode.com/problems/count-and-say

problem: 报数

solution: 模拟就完事了

*/

func next(s string) string {
	res := ""
	var pre byte = ' '
	cnt := 0
	for i := range s {
		if s[i] == pre {
			cnt++
		} else {
			if cnt != 0 {
				res += strconv.Itoa(cnt) + string(pre)
			}
			cnt=1
			pre = s[i]
		}
	}
	return res + strconv.Itoa(cnt) + string(pre)
}

func countAndSay(n int) string {
	t := "1"
	for i:=2;i<=n;i++ {
		t = next(t)
	}
	return t
}
