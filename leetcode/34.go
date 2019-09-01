/*

link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

problem: 求升序序列nums中target出现的区间，要求O(lgn)的时间复杂度

solution: 两次二分，先找首位，再找末位

*/

func searchRange(nums []int, target int) []int {
	if len(nums) < 1 {
		return []int{-1, -1}
	}
	l, r := 0, len(nums)-1
	for l < r {
		mid := (l + r) / 2
		if nums[mid] >= target {
			r = mid
		} else {
			l = mid + 1
		}
	}
	if nums[r] != target {
		return []int{-1, -1}
	}
	ll := r
	l, r = 0, len(nums)-1
	for l < r {
		mid := (l + r + 1) / 2
		if nums[mid] <= target {
			l = mid
		} else {
			r = mid - 1
		}
	}
	return []int{ll, r}
}
