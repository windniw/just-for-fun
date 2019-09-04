/*

link: https://leetcode.com/problems/combination-sum

problem: 完全背包

solution: DP就行了。不过用go写数组真是...噩梦

*/

type solution []int

func (s solution) add(n int) solution {
	r := make([]int, len(s))
	copy(r, s)
	return append(r, n)
}

func newSolution(nums ...int) solution {
	return nums
}

func combinationSum(candidates []int, target int) [][]int {
	dp := make([][]solution, target+1)
	dp[0] = []solution{newSolution()}
	for i := 0; i < len(candidates); i++ {
		for j := 1; j <= target; j++ {
			if j-candidates[i] >= 0 {
				for k := range dp[j-candidates[i]] {
					dp[j] = append(dp[j], dp[j-candidates[i]][k].add(candidates[i]))
				}
			}
		}
	}
	res := make([][]int, len(dp[target]))
	for i := 0;i<len(dp[target]); i++{
		res[i] = dp[target][i]
	}
	return res
}
