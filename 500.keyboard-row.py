#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#
# https://leetcode-cn.com/problems/keyboard-row/description/
#
# algorithms
# Easy (64.11%)
# Total Accepted:    5.2K
# Total Submissions: 8.1K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
#
#
#
#
#
#
#
# 示例：
#
# 输入: ["Hello", "Alaska", "Dad", "Peace"]
# 输出: ["Alaska", "Dad"]
#
#
#
#
# 注意：
#
#
# 你可以重复使用键盘上同一字符。
# 你可以假设输入的字符串将只包含字母。
#
#
class Solution:
    def findWords(self, words: 'List[str]') -> 'List[str]':
        res = []
        keyboard = ['QWERTYUIOPqwertyuiop', 'ASDFGHJKLasdfghjkl', 'ZXCVBNMzxcvbnm']
        for word in words:

            keys = keyboard[0]
            for i in keyboard[1:]:
                if word[0] in i:
                    keys = i

            flag = True
            for c in word:
                if c not in keys:
                    flag = False
                    break
            if flag:
                res.append(word)
        return res

# words = ["Hello", "Alaska", "Dad", "Peace"]

# print(Solution().findWords(words))
