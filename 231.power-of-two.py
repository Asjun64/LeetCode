#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (43.44%)
# Total Accepted:    10.7K
# Total Submissions: 24.6K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
#
# 示例 1:
#
# 输入: 1
# 输出: true
# 解释: 20 = 1
#
# 示例 2:
#
# 输入: 16
# 输出: true
# 解释: 24 = 16
#
# 示例 3:
#
# 输入: 218
# 输出: false
#
#
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        i = 1
        while i < n:
            i *= 2
        if i == n:
            return True
        else:
            return False
