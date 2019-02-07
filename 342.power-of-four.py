#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#
# https://leetcode-cn.com/problems/power-of-four/description/
#
# algorithms
# Easy (43.63%)
# Total Accepted:    5K
# Total Submissions: 11.4K
# Testcase Example:  '16'
#
# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
#
# 示例 1:
#
# 输入: 16
# 输出: true
#
#
# 示例 2:
#
# 输入: 5
# 输出: false
#
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
#
#
class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """

        # 位计算，最高位是奇数位，且其余位全为0时，即为4的幂
        if num <= 0:
            return False
        flag = True
        while num > 1:
            if num & 1 :
                return False
            num >>=1
            flag = not flag
        if flag:
            return True
        else:
            return False

        """
        # 2
        if num <= 0:
            return False
        while num >= 4:
            if num & 3 != 0:
                return False
            num >>= 2
        if num == 1:
            return True
        else:
            return False
        """

        """
        # 1
        if num <= 0:
            return False
        i = 1
        while i < num:
            i *= 4
        if i == num:
            return True
        else:
            return False
        """
# print(Solution().isPowerOfFour(16))