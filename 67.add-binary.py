#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (45.53%)
# Total Accepted:    14.6K
# Total Submissions: 32K
# Testcase Example:  '"11"\n"1"'
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 输入为非空字符串且只包含数字 1 和 0。
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
#
#
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

        """
        result = ""
        num_c = 0
        if len(a) < len(b) :
            a, b = b, a

        for i in range(1, len(b)+1):
            num_a = int(a[-i])
            num_b = int(b[-i])
            r = num_a ^ num_b ^ num_c
            c = num_a & num_b | num_a & num_c | num_b & num_c

            result = str(r) + result
            num_c = c

        for i in range(1, len(a)-len(b)+1):
            num_a = int(a[-(i+len(b))])

            r = num_a ^ num_c
            c = num_a & num_c

            result = str(r) + result
            num_c = c

        if (num_c == 1):
            result = '1' + result

        return result
        """


# s = Solution()

# arr_1 = ["0", "0", "1", "1", "100", "1010", "1111", "10010", "110"]
# arr_2 = ["0", "1", "0", "1", "101", "1001", "1001", "101", "11101"]

# for i in range(len(arr_1)):
#     print(s.addBinary(arr_1[i], arr_2[i]))

