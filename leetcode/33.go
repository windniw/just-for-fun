/*

link: https://leetcode.com/problems/search-in-rotated-sorted-array

problem: 一个不重复升序序列，从某点断开并互换前后段位置，求O(lgn)算法问某数是否存在于序列中

solution: 两次二分，先找断点，后找位置

*/

func search(nums []int, target int) int {
	if len(nums) == 0 {
		return -1
	}
	l, r := 1, len(nums)
	for l < r {
		mid := (l + r) / 2
		if nums[mid] > nums[0] {
			l = mid + 1
		} else {
			r = mid
		}
	}
	var (
		nl []int
		p  int
	)
	if target >= nums[0] {
		nl = nums[:r]
		p = 0
	} else {
		nl = nums[r:]
		p = r
	}
	t := sort.SearchInts(nl, target)
	if p+t < len(nums) && nums[p+t] == target {
		return p + t
	} else {
		return -1
	}
}
