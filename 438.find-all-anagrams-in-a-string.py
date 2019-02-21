#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (34.17%)
# Total Accepted:    3.1K
# Total Submissions: 8.8K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
#
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
#
# 说明：
#
#
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。
#
#
# 示例 1:
#
#
# 输入:
# s: "cbaebabacd" p: "abc"
#
# 输出:
# [0, 6]
#
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#
#
# 示例 2:
#
#
# 输入:
# s: "abab" p: "ab"
#
# 输出:
# [0, 1, 2]
#
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#
#
#

class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []

        res = []


        char_count_p = dict(zip(list('qwertyuiopasdfghjklzxcvbnm'), [0 for _ in range(26)]))
        for char in p:
            char_count_p[char] += 1

        char_count_window = dict(zip(list('qwertyuiopasdfghjklzxcvbnm'), [0 for _ in range(26)]))
        window_len = len(p)

        for c in s[:window_len]:
            char_count_window[c] += 1

        if char_count_window == char_count_p:
            res.append(0)

        for i in range(len(s) - window_len):
            char_count_window[s[i+window_len]] += 1
            char_count_window[s[i]] -= 1
            if char_count_window == char_count_p:
                res.append(i+1)

        return res


    def myFindAnagrams(self, s, p):
        res = []
        if len(s) < len(p):
            return res

        index = 0
        len_p = len(p)

        tmp = []

        d = {}
        for c in p:
            if d.get(c) != None:
                d[c].append(-1)
            else:
                d[c] = [-1]


        for index in range(len(s)):
            if d.get(s[index]) == None:
                for key in d.keys():
                    d[key] = [-1] * len(d[key])
                tmp = []
            else:
                li = d[s[index]]
                lastMin = min(li)
                li[li.index(lastMin)] = index


                if tmp and lastMin >= min(tmp) :
                    tmp = tmp[lastMin - tmp[0] + 1 :]
                tmp.append(index)

                if len(tmp) == len_p:
                    res.append(tmp[0])
        return res


# print(Solution().findAnagrams("abacbabc", "abc"))
