#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第N个数字
#
# https://leetcode-cn.com/problems/nth-digit/description/
#
# algorithms
# Easy (29.80%)
# Total Accepted:    2K
# Total Submissions: 6.6K
# Testcase Example:  '3'
#
# 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。
#
# 注意:
# n 是正数且在32为整形范围内 ( n < 231)。
#
# 示例 1:
#
#
# 输入:
# 3
#
# 输出:
# 3
#
#
# 示例 2:
#
#
# 输入:
# 11
#
# 输出:
# 0
#
# 说明:
# 第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。
#
#
#


class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        len = 0

        tmp = n
        while tmp > 0:
            len += 1
            tmp -= 9 * pow(10, len-1) * len

        cnt = tmp + 9 * pow(10, len-1) * len

        # 第 i 个数（从1计数）
        i = (cnt-1) // len
        # 第 j 位 （从右至左，从0计数）
        j = len - (cnt-1) % len - 1

        res = pow(10, len-1) + i
        while j:
            res //= 10
            j -= 1
        return int(res % 10)


# print(Solution().findNthDigit(3))
# print(Solution().findNthDigit(11))
# print(Solution().findNthDigit(188))
# print(Solution().findNthDigit(189))
# print(Solution().findNthDigit(190))
# print(Solution().findNthDigit(10000))
