/*

link: https://leetcode.com/problems/valid-sudoku

problem: 给一个数独，问当前状态是否合法

solution: 暴搜

*/

func byteToUint(b byte) uint {
	if b == '.' {
		return 0
	}
	return uint(b) - uint('0')
}

func merge(k1, k2 int) (int, bool) {
	if k2 == 1 {
		return k1, true
	}
	if k1&k2 != 0 {
		return 0, false
	}
	return k1 | k2, true
}

func cell(board [][]byte, row, col int) bool {
	res := 0
	for i := row; i < row+3; i++ {
		for j := col; j < col+3; j++ {
			var valid bool
			res, valid = merge(res, 1<<byteToUint(board[i][j]))
			if !valid {
				return false
			}
		}
	}
	return true
}

func col(board [][]byte, n int) bool {
	res := 0
	for i := 0; i < 9; i++ {
		var valid bool
		res, valid = merge(res, 1<<byteToUint(board[i][n]))
		if !valid {
			return false
		}
	}
	return true
}

func row(board [][]byte, n int) bool {
	res := 0
	for i := 0; i < 9; i++ {
		var valid bool
		res, valid = merge(res, 1<<byteToUint(board[n][i]))
		if !valid {
			return false
		}
	}
	return true
}

func isValidSudoku(board [][]byte) bool {
	for i := 0; i < 9; i++ {
		if !row(board, i) {
			return false
		}
		if !col(board, i) {
			return false
		}
	}
	return cell(board, 0, 0) && cell(board, 0, 3) && cell(board, 0, 6) &&
		cell(board, 3, 0) && cell(board, 3, 3) && cell(board, 3, 6) &&
		cell(board, 6, 0) && cell(board, 6, 3) && cell(board, 6, 6)
}
