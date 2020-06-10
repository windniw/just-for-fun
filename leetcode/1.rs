/// link: https://leetcode.com/problems/two-sum
/// problem: 数组中有两个元素相加等于target，返回其下标
/// solution: 暴力扫

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        for i in 0..nums.len() {
            for j in i + 1..nums.len() {
                if nums[i] + nums[j] == target {
                    return vec![i as i32, j as i32];
                }
            }
        }
        vec![]
    }
}
