/*

link: https://leetcode.com/problems/search-insert-position

problem: 有序数组，若存在target返回位置，反之返回应插入的位置

solution: 基础二分

*/

func searchInsert(nums []int, target int) int {
	l, r := 0, len(nums)-1
	for l <= r {
		mid := (l + r) / 2
		if nums[mid] < target {
			l = mid + 1
		} else if nums[mid] > target {
			r = mid - 1
		} else {
			return mid
		}
	}
	return l
}