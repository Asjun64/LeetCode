#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#
# https://leetcode-cn.com/problems/perfect-number/description/
#
# algorithms
# Easy (32.04%)
# Total Accepted:    3.5K
# Total Submissions: 10.5K
# Testcase Example:  '28'
#
# 对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
#
# 给定一个 正整数 n， 如果他是完美数，返回 True，否则返回 False
#
#
#
# 示例：
#
#
# 输入: 28
# 输出: True
# 解释: 28 = 1 + 2 + 4 + 7 + 14
#
#
#
#
# 注意:
#
# 输入的数字 n 不会超过 100,000,000. (1e8)
#
#
import math
class Solution:
    def checkPerfectNumber(self, num: 'int') -> 'bool':
        if num < 2:
            return False
        sons = []
        for i in range(1, int(math.sqrt(num))+1):
            if num % i == 0:
                sons.extend([i, num // i])

        return sum(sons) == num * 2

# print(Solution().checkPerfectNumber(1))