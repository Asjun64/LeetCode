#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (45.62%)
# Total Accepted:    5.9K
# Total Submissions: 12.9K
# Testcase Example:  '"hello"'
#
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
# 示例 1:
#
# 输入: "hello"
# 输出: "holle"
#
#
# 示例 2:
#
# 输入: "leetcode"
# 输出: "leotcede"
#
# 说明:
# 元音字母不包含字母"y"。
#
#
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = [i for i in s]
        i = 0
        j = len(s)-1
        while i < j :
            while i < j and not self.isVowel(s[i]):
                i += 1
            while i < j and not self.isVowel(s[j]):
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)

    def isVowel(self, c):
        if c in "aeiouAEIOU" :
            return True
        return False

# print(Solution().reverseVowels("hello"))

