#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#
# https://leetcode-cn.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (45.42%)
# Total Accepted:    3.2K
# Total Submissions: 7K
# Testcase Example:  '"abccccdd"'
#
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
#
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
#
# 注意:
# 假设字符串的长度不会超过 1010。
#
# 示例 1:
#
#
# 输入:
# "abccccdd"
#
# 输出:
# 7
#
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
#
#
#
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = len(s)
        d = dict.fromkeys(s, 0)
        for one in s:
            d[one] += 1
        first = True
        for one in d:
            if d[one] % 2 == 1:
                if first:
                    first = False
                else:
                    res -= 1
        return res



# print(Solution().longestPalindrome("a"))

