#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
# https://leetcode-cn.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (42.18%)
# Total Accepted:    6.2K
# Total Submissions: 14.7K
# Testcase Example:  '"egg"\n"add"'
#
# 给定两个字符串 s 和 t，判断它们是否是同构的。
#
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
#
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
#
# 示例 1:
#
# 输入: s = "egg", t = "add"
# 输出: true
#
#
# 示例 2:
#
# 输入: s = "foo", t = "bar"
# 输出: false
#
# 示例 3:
#
# 输入: s = "paper", t = "title"
# 输出: true
#
# 说明:
# 你可以假设 s 和 t 具有相同的长度。
#
#
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.fun(s,t) and self.fun(t, s)

    def fun(self, s, t):
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            elif d[s[i]] != t[i]:
                return False
        return True

# s = Solution()

# arr = ["ab", "ba"]

# print(s.isIsomorphic(arr[0], arr[1]))