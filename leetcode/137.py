"""

link: https://leetcode.com/problems/single-number-ii

problem: 给定数组，只有一个数字出现1次，其他都是3次，找到1次的数字，要求空间O(1)

solution: 这题其实很有难度。先类比136题，处理空间O(1)上使用了异或，实际上是二进制上不进位的加法。
          本质上136的解决思路是，用一个数的每一个二进制位，单独来代表这个数组中，这一位上，1的数量，
          如果是奇数就是1，偶数就是0，这样最后结果肯定会留下所有奇数的位，则为所求值。
          那么举一反三，这题的解决思路是，定义一种运算，来标记这个数组中，每个二进制位上，1的数量，每
          出现3次就清零，最后留下所有只出现一次的位，则为所求值。
          处理上，也不需要定义运算，直接使用二进制加法即可 
          [ 00 + 1 = 01; 01 + 1 = 10; 10 + 1 = 11; 11 ==> 00
            00 + 0 = 00; 01 + 0 = 01; 10 + 0 = 10 ]
          对每一位，用 one 和 two 的对应位来共同标记其值
          出现 0 次时，one[k] = 0, two[k] = 0
          出现 1 次时，one[k] = 0, two[k] = 1
          出现 2 次时，one[k] = 1, two[k] = 0
          出现 3 次时，one[k] = 1, two[k] = 1，当出现此组合时，立即重置 one[k] = two[k] = 0
          更直观的描述此运算为:
          if one[k] = 1 and two[k] = 0:
              two[k] ^= x
          if one[k] = 0 || one[k] == 1:
              one[k] ^= x:
          if one[k] = 1 and two[k] = 1:
              one[k] = two[k] = 0

solutuon-fix: 第一种做法是在得到 11 后，再重置为 00，事实上这一步也可以省略掉，定义运算为:
              [ 00 + 1 = 01; 01 + 1 = 10; 10 + 1 = 00;
                00 + 0 = 00; 01 + 0 = 01; 10 + 0 = 10 ]
              if one[k] == 1 || one[k] == 0:
                  one[k] ^= x 
              if two[k] = 1:
                  one[k] = 0
              if two[k] == 1 || two[k] == 0:
                  two[k] ^= x
              if one[k] = 1:
                  two[k] = 0

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for x in nums:
            two ^= one & x
            one ^= x
            t = one & two
            one &= ~t
            two &= ~t
        return one

#---
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for x in nums:
            one = one ^ x & ~two
            two = two ^ x & ~one
        return one