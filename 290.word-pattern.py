#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词模式
#
# https://leetcode-cn.com/problems/word-pattern/description/
#
# algorithms
# Easy (36.48%)
# Total Accepted:    4.3K
# Total Submissions: 11.8K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# 给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。
#
# 这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。
#
# 示例1:
#
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
#
# 示例 2:
#
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
#
# 示例 3:
#
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
#
# 示例 4:
#
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
#
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
#
#
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        if len(pattern) != len(str):
            return False
        d = {}
        for i in range(len(str)):
            m = pattern[i] in d
            n = str[i] in d.values()
            if m and n :
                if d[pattern[i]] != str[i]:
                    return False
                else:
                    continue
            elif m or n:
                return False
            else:
                d[pattern[i]] = str[i]
        return True


# print(Solution().wordPattern("abba", "dog cat cat dog"))
