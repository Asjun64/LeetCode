#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#
# https://leetcode-cn.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (28.21%)
# Total Accepted:    3.3K
# Total Submissions: 11.7K
# Testcase Example:  '"Hello, my name is John"'
#
# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
#
# 请注意，你可以假定字符串里不包括任何不可打印的字符。
#
# 示例:
#
# 输入: "Hello, my name is John"
# 输出: 5
#
#
#
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = False
        cnt = 0
        for i in s:
            if not start and i != ' ':
                start = True
            elif start and i == ' ':
                start = False
                cnt += 1
        if len(s) > 0 and s[-1] != ' ':
            cnt += 1
        return cnt

# print(Solution().countSegments("aaaa"))