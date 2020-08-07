"""

link: https://leetcode-cn.com/problems/integer-to-english-words

problem: 非负整数转英文表示

solution: 模拟。每千位转一次。

"""
class Solution:
    def numberToWords(self, num: int) -> str:
        m = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion",
        }

        def f(x: int, unit: str):
            if x == 0:
                return ""
            res = []
            if x >= 100:
                res.append(m[x // 100])
                res.append(m[100])
            x %= 100
            if 0 < x <= 20:
                res.append(m[x])
            elif x > 20:
                res.append(m[x // 10 * 10])
                if x % 10 != 0:
                    res.append(m[x % 10])
            return " ".join(res) + " " + unit + " "

        if num == 0:
            return "Zero"
        return (f(num // 10 ** 9, m[10 ** 9]) + f(num % 10 ** 9 // 10 ** 6, m[10 ** 6]) + f(
            num % 10 ** 6 // 10 ** 3, m[10 ** 3]) + f(num % 10 ** 3, "")).strip()
