#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#
# https://leetcode-cn.com/problems/base-7/description/
#
# algorithms
# Easy (41.17%)
# Total Accepted:    2.4K
# Total Submissions: 5.8K
# Testcase Example:  '100'
#
# 给定一个整数，将其转化为7进制，并以字符串形式输出。
#
# 示例 1:
#
#
# 输入: 100
# 输出: "202"
#
#
# 示例 2:
#
#
# 输入: -7
# 输出: "-10"
#
#
# 注意: 输入范围是 [-1e7, 1e7] 。
#
#
class Solution:
    def convertToBase7(self, num: 'int') -> 'str':
        if num == 0:
            return '0'

        res = []

        isNeg = num < 0
        num = abs(num)

        while num :
            res.append(str(num % 7))
            num //= 7
        if isNeg:
            res.append('-')
        res.reverse()
        return "".join(res)


# print(Solution().convertToBase7(-0))
