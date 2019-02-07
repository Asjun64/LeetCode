#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (28.26%)
# Total Accepted:    15.4K
# Total Submissions: 54.6K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
#
# 如果不存在最后一个单词，请返回 0 。
#
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
#
# 示例:
#
# 输入: "Hello World"
# 输出: 5
#
#
#
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split()
        if (len(l) > 0):
            return len(l[-1])
        else :
            return 0


        """
        isStart = False
        for i in s[::-1]:
            if not isStart and i != ' ':
                isStart = True
                cnt = 1
            elif isStart and i != ' ':
                cnt += 1
            elif isStart and i == ' ':
                break
        return cnt
        """


# s = Solution()
# arr = ["Hello World", "      ", "Asjun", "fjdka fda aa", "a "]
# for i in arr:
#     print(s.lengthOfLastWord(i))

