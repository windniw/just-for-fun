/*

link: https://leetcode.com/problems/maximum-subarray

problem: 基础DP

solution: 基础DP，扫一遍完事

*/

func maxSubArray(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	s, max := 0, nums[0]
	empty := true
	for i := range nums {
		empty = false
		s += nums[i]
		if !empty && s > max {
			max = s
		}
		if s <= 0 {
			empty = true
			s = 0
		}
	}
	if !empty && s > max {
		max = s
	}
	return max
}
