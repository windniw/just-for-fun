`
见 406.py

及学习Go这么奇特且不优雅但实用的插入方式
`

func reconstructQueue(people [][]int) [][]int {
	length := len(people)
	sort.Slice(people, func(a, b int) bool {
		return !(people[a][0] < people[b][0] || people[a][0] == people[b][0] && people[a][1] > people[b][1])
	})
	var newPeoPle [][]int
	for i := 0; i < length; i++ {
		k := people[i][1]
		newPeoPle = append(newPeoPle, []int{0, 0})
		copy(newPeoPle[k+1:], newPeoPle[k:])
		newPeoPle[k] = people[i]
	}
	return newPeoPle
}