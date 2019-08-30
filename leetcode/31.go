/*

link: https://leetcode.com/problems/next-permutation

problem: 给数组nums，求next(nums)，定义next为nums的所有元素升序排列后，当前nums状态的下一位
         若已为最后一位，则输出最小序列

solution: 倒序遍历，找到第一个降序点的位置j，swap(nums[j], nums[k])，其中k为nums[j+1:len]中大于
          nums[j]的最小值，然后重排序nums[j+1:len]。时间复杂度为 O(n+n+nlgn) --> O(nlgn)

solution-fix: 前部分逻辑不变，将重排序修改遍历翻转，因为本来就是纯降序列，时间复杂度优化为O(n)

*/

func nextPermutation(nums []int) {
	if len(nums) < 2 {
		return
	}
	for i := len(nums) - 2; i >= 0; i-- {
		if nums[i] < nums[i+1] {
			min := i + 1
			for j := i + 2; j < len(nums); j++ {
				if nums[j] > nums[i] && nums[min] > nums[j] {
					min = j
				}
			}
			nums[i], nums[min] = nums[min], nums[i]
			sort.Ints(nums[i+1:])
			return
		}
	}
	sort.Ints(nums)
	return
}

// ---

func nextPermutation(nums []int) {
	if len(nums) < 2 {
		return
	}
	for i := len(nums) - 2; i >= 0; i-- {
		if nums[i] < nums[i+1] {
			min := i + 1
			for j := i + 2; j < len(nums); j++ {
				if nums[j] > nums[i] && nums[min] >= nums[j] {
					min = j
				}
			}
			nums[i], nums[min] = nums[min], nums[i]
			for j := i + 1; j < i+1+(len(nums)-i)/2; j++ {
				nums[j], nums[len(nums)-1-(j-(i+1))] = nums[len(nums)-1-(j-(i+1))], nums[j]
			}
			return
		}
	}
	sort.Ints(nums)
	return
}

