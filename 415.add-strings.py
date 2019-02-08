#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (42.34%)
# Total Accepted:    4.3K
# Total Submissions: 10.1K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
# 注意：
#
#
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
#
#
#
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = ""
        c = 0
        NUMS = "0123456789"
        for i in range(1, min(len(num1), len(num2))+1):
            sum = NUMS.index(num1[-i]) + NUMS.index(num2[-i]) + c
            r = str(sum % 10)
            c = sum // 10
            result = r + result
        for i in range(len(result)+1, len(num1)+1):
            sum = NUMS.index(num1[-i]) + c
            r = str(sum % 10)
            c = sum // 10
            result = r + result
        for i in range(len(result)+1, len(num2)+1):
            sum = NUMS.index(num2[-i]) + c
            r = str(sum % 10)
            c = sum // 10
            result = r + result
        if c != 0 :
            result = str(c) + result
        return result

# num1 = "98"
# num2 = "9"

# print(Solution().addStrings(num1, num2))
