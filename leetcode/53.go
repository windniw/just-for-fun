/*

link: https://leetcode.com/problems/maximum-subarray

problem: 求序列nums的最长子串和

solution: 
dp[i]定义为以i结尾的子串的最大和，转移方程为：dp[i] = max(dp[i-1] + nums[i], nums[i])
因为dp[i]只跟dp[i-1]关联，状态压缩一下不记录更早的值，扫一遍完事

*/

func maxSubArray(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	s, max := 0, nums[0]
	for i := range nums {
		if s < 0 {
			s = nums[i]
		} else {
			s += nums[i]
		}
		if s > max {
			max = s
		}
	}
	return max
}

