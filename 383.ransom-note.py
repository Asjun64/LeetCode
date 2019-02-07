#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
# https://leetcode-cn.com/problems/ransom-note/description/
#
# algorithms
# Easy (44.18%)
# Total Accepted:    4.2K
# Total Submissions: 9.4K
# Testcase Example:  '"a"\n"b"'
#
# 给定一个赎金信 (ransom)
# 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true
# ；否则返回 false。
#
# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)
#
# 注意：
#
# 你可以假设两个字符串均只含有小写字母。
#
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
#
#
#
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d_ramdom = self.fun(ransomNote)
        d_magazine = self.fun(magazine)

        for key in d_ramdom:
            if key in d_magazine and d_magazine[key] >= d_ramdom[key]:
                continue
            else:
                return False
        return True

    def fun(self, li):
        d = {}
        for c in li:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        return d

# print(Solution().canConstruct("aa", "aab"))

