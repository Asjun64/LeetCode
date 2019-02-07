#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (33.81%)
# Total Accepted:    20.8K
# Total Submissions: 61.4K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
#
#
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
# 由于返回类型是整数，小数部分将被舍去。
#
#
#
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x <= 1:
            return x
        r = x
        while r > x / r:
            r = (r + x / r) // 2
        return int(r)

        """
        guess = 1.0
        old_guess = x
        while abs(old_guess - guess) >= 1:
            old_guess = guess
            guess = (guess + x/guess) / 2
        return int(guess)
        """

# s = Solution()
# for i in range(1, 30, 3):
#     print(str(i) + "\t" + str(s.mySqrt(i)))

