/// link: https://leetcode.com/problems/two-sum
/// problem: 数组中有两个元素相加等于target，返回其下标
/// solution: 暴力扫
/// solution-fix: 用map存取已扫描过的值

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

// ---
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        use std::collections::HashMap;
        let mut m: HashMap<i32, i32> = HashMap::new();
        for i in 0..nums.len() {
            if m.contains_key(&(target - nums[i])) {
                return vec![i as i32, m[&(target - nums[i])]];
            }
            m.insert(nums[i], i as i32);
        }
        vec![]
    }
}
