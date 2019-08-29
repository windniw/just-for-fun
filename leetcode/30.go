/*

link: https://leetcode.com/problems/substring-with-concatenation-of-all-words

problem: 给定字符串s，若干定长词words，求s中所有满足条件子串s'，s'可通过words的所有词组合得到

solution: 起map，暴力检查每个长度为sum(len(words[i]))的子串

solution-fix: 照样存map，分类讨论，优化剪枝

*/
func findSubstring(s string, words []string) []int {
	if len(s) == 0 || len(words) == 0 {
		return []int{}
	}
	baseLen := len(words[0])
	l := 0
	kmap := make(map[string]int)
	res := []int{}
	for _, w := range words {
		l += len(w)
		kmap[w]++
	}

	for i := 0; i <= len(s)-l; i++ {
		kkmap := make(map[string]int)
		for k, v := range kmap {
			kkmap[k] = v
		}

		f := func() bool {
			for j := i; j < i+l; j += baseLen {
				str := s[j : j+baseLen]
				if val, exist := kkmap[str]; exist && val > 0 {
					kkmap[str]--
				} else {
					return false
				}
			}
			return true
		}

		if f() {
			res = append(res, i)
		}
	}
	return res
}

// ---

func findSubstring(s string, words []string) []int {
	if len(s) == 0 || len(words) == 0 {
		return []int{}
	}
	baseLen := len(words[0])
	l := 0
	kmap := make(map[string]int)
	res := []int{}
	for _, w := range words {
		l += len(w)
		kmap[w]++
	}

	for i := 0; i <= len(s)-l && i < baseLen; i++ {
		kkmap := make(map[string]int)
		for k, v := range kmap {
			kkmap[k] = v
		}

		f := func(bp int, curp int) (bool, int) {
			for j := curp; j < bp+l; j += baseLen {
				str := s[j : j+baseLen]
				if val, exist := kkmap[str]; exist && val > 0 {
					kkmap[str]--
				} else {
					return false, j
				}
			}
			return true, bp + l
		}

		beginPos, curPos := i, i
		for beginPos <= len(s)-l {
			if match, endPos := f(beginPos, curPos); match {
				res = append(res, beginPos)
				kkmap[s[beginPos:beginPos+baseLen]]++
				beginPos += baseLen
				curPos = endPos
			} else {
				if _, exist := kkmap[s[endPos:endPos+baseLen]]; !exist {
					for k := beginPos; k < endPos; k += baseLen {
						kkmap[s[k:k+baseLen]]++
					}
					beginPos = endPos + baseLen
					curPos = beginPos
				} else {
					for {
						if s[beginPos:beginPos+baseLen] == s[endPos:endPos+baseLen] {
							beginPos += baseLen
							break
						} else {
							kkmap[s[beginPos:beginPos+baseLen]]++
							beginPos += baseLen
						}
					}
					curPos = endPos + baseLen
				}
			}
		}
	}
	return res
}

