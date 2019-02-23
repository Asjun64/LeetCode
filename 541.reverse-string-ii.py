#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#
# https://leetcode-cn.com/problems/reverse-string-ii/description/
#
# algorithms
# Easy (43.24%)
# Total Accepted:    3K
# Total Submissions: 6.9K
# Testcase Example:  '"abcdefg"\n2'
#
# 给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k
# 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。
#
# 示例:
#
#
# 输入: s = "abcdefg", k = 2
# 输出: "bacdfeg"
#
#
# 要求:
#
#
# 该字符串只包含小写的英文字母。
# 给定字符串的长度和 k 在[1, 10000]范围内。
#
#
#
import math
class Solution:
    def reverseStr(self, s: 'str', k: 'int') -> 'str':
        res = []
        isReverse = True
        i = 0
        while i < len(s)//k:
            if isReverse:
                if i*k-1 == -1:
                    res.append(s[i*k+k-1::-1])
                else:
                    res.append(s[i*k+k-1:i*k-1:-1])
                isReverse = False
            else:
                res.append(s[i*k:i*k+k])
                isReverse = True
            i += 1
        if isReverse:
            if i*k-1 == -1:
                res.append(s[-1::-1])
            else:
                res.append(s[-1:i*k-1:-1])
        else:
            res.append(s[i*k:])
        return "".join(res)

# s = 'a'
# k = 2

# print(s)
# print(Solution().reverseStr(s, k))

